import cv2 as cv

from app.adb import tap
from app.utils import ImageComparison, take_screenshot, get_last_screenshot_path, stop, wait
from log.log import logger
from pages.targets import Targets


# is_*_on_screen

def is_target_on_screen(target, number_of_attempts=1):
    # todo переписать эту функцию без использования класса ImageComparison

    for _ in range(number_of_attempts):
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            return True

        if number_of_attempts > 1:
            take_screenshot()

    else:
        logger.info(f"Target {target} did not found after {number_of_attempts} attempts")
        return False


def is_button_get_on_screen() -> bool:
    target = Targets.button_get
    return is_target_on_screen(target)


def is_button_ok_on_screen() -> bool:
    target = Targets.button_ok
    return is_target_on_screen(target)


def is_button_repeat_on_screen() -> bool:
    target = Targets.button_repeat
    return is_target_on_screen(target)


def is_loader_on_screen() -> bool:
    target = Targets.loader
    return is_target_on_screen(target, number_of_attempts=1)


def is_google_play_on_screen() -> bool or None:
    for target in Targets.google_play_targets:
        if is_target_on_screen(target):
            return True


# find_and_tap

def find_and_tap(target_path, img_path=None, method=5, threshold=0.87, number_of_attempts=1):
    target = cv.imread(target_path, 0)

    for attempt in range(number_of_attempts):
        # debug
        if img_path:
            img = cv.imread(img_path, 0)
        else:
            img = cv.imread(get_last_screenshot_path(), 0)
        logger.info(f"Ищем: {target_path}")
        result = cv.matchTemplate(img, target, method)
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            logger.info("Target detected")
            break

        logger.info(f"{attempt + 1} attempt")
        take_screenshot()

    else:
        logger.info(f"Target not found. {number_of_attempts} attempts. Value: {max_val}")
        return

    x, y = max_loc
    h, w = target.shape
    tap(x + w // 2, y + h // 2)


def tap_button_get():
    target = Targets.button_get
    find_and_tap(target)


def tap_button_ok():
    target = Targets.button_ok
    find_and_tap(target)


def tap_button_repeat():
    target = Targets.button_repeat
    find_and_tap(target)


# find, tap and check

def find_tap_and_check(target, check_func):
    find_and_tap(target)
    wait(1)
    for attempt in range(5):
        logger.info(f"{attempt} попытка")
        take_screenshot()
        if check_func:
            return True


def tap_button_get_and_check(check_func):
    # tap_button_get()
    # wait(1)
    # for attempt in range(5):
    #     logger.info(f"{attempt} попытка")
    #     take_screenshot()
    #     if check_func:
    #         return True
    target = Targets.button_get
    return find_tap_and_check(target, check_func)

def tap_button_ok_and_check(check_func):
    tap_button_ok()
    wait(1)
    for attempt in range(5):
        logger.info(f"{attempt} попытка")
        take_screenshot()
        if check_func:
            return True


# miscellaneous

def back_and_check(check_func, to_take_new_screenshot=False):
    if to_take_new_screenshot:
        take_screenshot()

    targets = Targets.back_buttons
    for target in targets:
        if is_target_on_screen(target):
            find_and_tap(target)
            wait(1)
            take_screenshot()
            break

    if check_func():
        logger.info("Удачно вернулись в предыдущее меню\n")
    else:
        logger.error("Не получилось вернутся в предыдущее меню")
        stop()

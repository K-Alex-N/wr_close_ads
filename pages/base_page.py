import sys
import time

import cv2 as cv

from app.adb import tap, tap_back
from app.utilites import ImageComparison, take_screenshot, get_last_screenshot_path, stop, wait
from log.log import logger
from pages.menu_specials import is_menu_special
from pages.targets import Targets


# is_*_on_screen ____________________

def is_target_on_screen(target, number_of_attempts=1):
    # logger.info(f"Ищем: {target}")

    # todo переписать эту функцию без использования класса ImageComparison
    if number_of_attempts == 1:
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            return True
    else:
        for _ in range(number_of_attempts):
            img_comp_obj = ImageComparison(target)
            if img_comp_obj.is_target_on_image():
                return True
            take_screenshot() # todo это должно быть только если несколько раз повторяем

        logger.info(f"Target {target} did not found after {number_of_attempts} attempts")
    return False


def is_button_get_on_screen():
    target = Targets.button_get
    return is_target_on_screen(target)

def is_button_ok_on_screen():
    target = Targets.button_ok
    return is_target_on_screen(target)

def is_button_repeat_on_screen():
    target = Targets.button_repeat
    return is_target_on_screen(target)


def is_loader_on_screen():
    target = Targets.loader
    return is_target_on_screen(target, number_of_attempts=1)


def is_google_play():
    for target in Targets.google_play_targets:
        if is_target_on_screen(target, number_of_attempts=1):
            return True


# find_and_tap ____________________

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

# find, tap and check ____________________

def find_tap_and_check(target, check_func):
    find_and_tap(target)
    wait(1)
    for attempt in range(5):
        logger.info(f"{attempt} попытка")
        take_screenshot()
        if check_func:
            return True

def tap_button_get_and_check(check_func):
    tap_button_get()
    wait(1)
    for attempt in range(5):
        logger.info(f"{attempt} попытка")
        take_screenshot()
        if check_func:
            return True

def tap_button_ok_and_check(check_func):
    tap_button_ok()
    wait(1)
    for attempt in range(5):
        logger.info(f"{attempt} попытка")
        take_screenshot()
        if check_func:
            return True

# Miscellaneous ____________________

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
        logger.info("Не получилось вернутся в предыдущее меню\n")
        stop()


def watch_and_close_ad(check_func):
    logger.info("Начался просмотр рекламы\n")
    targets = Targets.for_closing_ads()
    start_time = time.time()
    while time.time() - start_time < 90:
        take_screenshot()
        for target in targets:
            # if is_target_on_screen(targets, threshold=0.8):

            img_comp_obj = ImageComparison(target, threshold=0.8)
            if img_comp_obj.is_target_on_image():
                img_comp_obj.tap_on_target()
                wait(2)
                take_screenshot()
                # нужно перезапустить while с начала + скриншот получить!
                break
        # else: # если прошли по всем таршетам и не нашли как заурыть рекламу то повторяем, пока не кончится время
        #     continue  # todo с помощью такой схемы попадаем в цикл



        # мб добавить проверку на RESUME и затем ждать 25 секунд
        # можно ли системную кнопку back назать если RESUME появилось

        if check_func():
            logger.info("Реклама закончилась. Вернулись в меню.")
            break

        if is_google_play():
            tap_back()
            wait(1)

    else:
        logger.error("За 90 секунд не получилось закрыть рекламу")
        stop()

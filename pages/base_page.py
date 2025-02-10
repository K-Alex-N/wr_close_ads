import sys
import time

import cv2 as cv

from app.adb import tap, tap_back
from app.utilites import ImageComparison, take_screenshot, get_last_screenshot_path, stop
from log.log import logger
from pages.menu_specials import is_menu_special
from pages.targets import Targets


# is_*_on_screen ____________________

def is_target_on_screen(target, number_of_attempts=2):
    logger.info(f"Ищем: {target}")

    # todo переписать эту функцию без использования класса ImageComparison

    for _ in range(number_of_attempts):
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            return True
        take_screenshot()

    logger.info(f"Target {target} did not found after {number_of_attempts} attempts")
    return False


def is_button_get_on_screen():
    target = Targets.button_get
    return is_target_on_screen(target)


def is_button_repeat_on_screen():
    target = Targets.button_repeat
    return is_target_on_screen(target)


def is_loader_on_screen():
    target = Targets.loader
    return is_target_on_screen(target)


def is_google_play():
    for target in Targets.google_play_targets:
        if is_target_on_screen(target, number_of_attempts=1):
            return True


# find_and_tap ____________________

def find_and_tap(target_path, img_path=None, method=5, threshold=0.87, number_of_attempts=2):
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


# Miscellaneous ____________________

def back_with_check(check_func, to_take_new_screenshot=True):
    if to_take_new_screenshot:
        take_screenshot()

    target = Targets.button_back
    find_and_tap(target)

    if check_func():
        logger.info("Удачно вернулись в предыдущее меню")
    else:
        logger.info("Не получилось вернутся в предыдущее меню")
        stop()

def watch_and_close_ad(check_func):
    logger.info("Начался просмотр рекламы")
    targets = Targets.for_closing_ads()
    start_time = time.time()
    while True:
        take_screenshot()
        for target in targets:
            # if is_target_on_screen(targets, threshold=0.8):

            img_comp_obj = ImageComparison(target, threshold=0.8)
            if img_comp_obj.is_target_on_image():
                img_comp_obj.tap_on_target()
                break

        # мб добавить проверку на RESUME и затем ждать 25 секунд

        if is_google_play():
            tap_back()

        if check_func():
            logger.info("Реклама закончилась. Снова в текущем меню.")
            break

        ad_time = time.time() - start_time
        logger.info(f"реклама длится: {ad_time} секунд")
        if ad_time > 90:
            logger.error("за 90 секунд не получилось закрыть рекламу")
            stop()
            break

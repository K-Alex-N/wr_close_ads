import sys
import time

import cv2 as cv
import numpy as np

from app.adb import tap, tap_system_button_back
from app.screenshot import take_screenshot, get_last_screenshot_path
from log.logger import logger
from pages.targets import Targets


def is_target_on_screen(target_path, threshold=0.8, method=5):
    logger.info(f"Ищем: {target_path}")

    target = cv.imread(target_path, 0)
    img = cv.imread(get_last_screenshot_path(), 0)

    result = cv.matchTemplate(img, target, method)
    _, max_val, _, _ = cv.minMaxLoc(result)

    if max_val >= threshold:
        return True

    logger.info(f"Target ({target_path}) did not found. Value: {max_val}")
    return False


def find_and_tap(target_path, method=5, threshold=0.8, number_of_attempts=1):
    logger.info(f"Ищем: {target_path}")
    target = cv.imread(target_path, 0)

    for _ in range(number_of_attempts):

        img = cv.imread(get_last_screenshot_path(), 0)
        result = cv.matchTemplate(img, target, method)
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            logger.info("Target detected")
            break

        take_screenshot()

    else:
        logger.info(f"Target not found. {number_of_attempts} attempts. Value: {max_val}")
        return

    x, y = max_loc
    h, w = target.shape
    tap(x + w // 2, y + h // 2)


def find_tap_and_check(target, check_func):
    find_and_tap(target)
    wait(1, "Ждем загрузку страницы")
    for attempt in range(3):
        logger.info(f"{attempt + 1} попытка проверки условия: {check_func}")
        take_screenshot()
        if check_func():
            logger.info(f"Условие {check_func} выполнено.")
            return True
    else:
        logger.error(f"Условие {check_func} не выполнено. Было {attempt + 1} попытки")
        stop()


def tap_all_buttons_on_screen(check_func, act_func, success_msg):
    while True:
        take_screenshot()
        if check_func():
            act_func()
            wait(0.5)
            continue
        else:
            logger.info(success_msg)
            break


def stop():
    logger.error("Остановка программы")
    sys.exit()


def wait(sec: float, msg: str = ""):
    logger.info(f"{msg} {sec} секунд. ")
    time.sleep(sec)


def is_color_similar(pixel_color, target_color, tolerance=3):
    for i in range(3):  # 3 цвета. BGR
        if target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance:
            continue
        return False
    return True


def get_coords_of_active_button():
    """"
    на текущем экране ищем активные кнопки
    """
    target = Targets.SpecialsMenu.button_watch
    img_color = cv.imread(get_last_screenshot_path())
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    target_color = cv.imread(target)
    first_pixel_target_color = target_color[0, 0]
    target_grey = cv.imread(target, 0)
    w, h = target_grey.shape[::-1]

    res = cv.matchTemplate(img_gray, target_grey, cv.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        x, y = pt[0], pt[1]
        pixel_color = img_color[y, x]
        if is_color_similar(pixel_color, first_pixel_target_color):
            return x + w, y + h
    return None


def watch_and_close_ad(check_func):
    from pages.common import is_resume_on_screen, tap_button_resume, is_google_play_on_screen

    logger.info("\nНачался просмотр рекламы")
    wait(5, "Ждем загрузку рекламы и пропускаем начало")
    targets = Targets.for_closing_ads()

    start_time = time.time()
    while time.time() - start_time < 120:
        take_screenshot()

        if is_resume_on_screen():  # значит крестик закрытия рекламы появляется до окончания времени
            tap_button_resume()
            wait(25, "Ждем примерное окончание рекламы")

        if check_func():
            logger.info("Реклама закончилась. Вернулись в меню.\n")
            break

        if is_google_play_on_screen():
            tap_system_button_back()
            wait(1, "Ждем загрузку страницы")

        for target in targets:
            if is_target_on_screen(target):
                find_and_tap(target)
                wait(2, "Ждем загрузку страницы")
                break

    else:
        logger.error("За 120 секунд не получилось закрыть рекламу")
        stop()


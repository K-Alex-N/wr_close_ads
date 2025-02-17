import sys
import time

import cv2 as cv
import numpy as np

from app.adb import tap, tap_system_button_back
from app.screenshot import take_screenshot, get_last_screenshot_path
from log.log import logger

from pages.targets import Targets


def is_target_on_screen(target_path, threshold=0.8, method=5, number_of_attempts=1):
    # for _ in range(number_of_attempts):
    target = cv.imread(target_path, 0)
    img = cv.imread(get_last_screenshot_path(), 0)
    logger.info(f"Ищем: {target_path}")

    result = cv.matchTemplate(img, target, method)
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    if max_val >= threshold:
        return True
    return False

    # logger.info(f"{attempt + 1} attempt")
    # take_screenshot()

    # img_comp_obj = ImageComparison(target)
    # if img_comp_obj.is_target_on_image():
    #     return True

    # if number_of_attempts > 1:
    #     take_screenshot()

    # else:
    #     logger.info(f"Target {target} did not found after {number_of_attempts} attempts")
    #     return False


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


def find_tap_and_check(target, check_func):
    find_and_tap(target)
    wait(1)
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
            continue
        else:
            logger.info(success_msg)
            break


def stop():
    logger.error("Остановка программы")
    sys.exit()


def create_low_and_height_color(button_color):
    low_color = []
    height_color = []
    for color in button_color:
        low_color.append(color - 2)
        height_color.append(color + 2)
    return low_color, height_color


# def tap_button_watch2():
#     target = f"{TARGETS_DIR}watch.png"
#     img = "images/screenshots/specials.png"
#     img = cv.imread(img, 0)
#     img2 = img.copy()
#     target = cv.imread(target, 0)
#     w, h = target.shape[::-1]
#
#     methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
#                'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']
#
#     for meth in methods:
#         img = img2.copy()
#         method = getattr(cv, meth)
#
#         print(method)
#
#         result = cv.matchTemplate(img, target, method)
#         min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
#         print(f"Method:{method} = {max_val}")
#
#         # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#         if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
#             top_left = min_loc
#         else:
#             top_left = max_loc
#         print(top_left)
#         bottom_right = (top_left[0] + w, top_left[1] + h)

# threshold = 0.9
# if max_val >= threshold:
#     logger.info("Target detected")
#     return True
# logger.error("Target not found")
# return False


def tap_button_watch():
    target = Targets.SpecialsMenu.button_watch
    method = 1  # TM_SQDIFF_NORMED
    # for method in [1, 5]:
    # img = "images/screenshots/specials.png"
    for _ in range(30):
        take_screenshot()

        if is_target_on_screen(target):
            find_and_tap(target)
        img_comp_obj = ImageComparison(target, method=method)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()
            return
        else:
            wait(1)
            continue


# def tap_button_watch3():
#     # сделать повторение т.к. кнопка watch может появиться не сразу
#
#     target = f"{TARGETS_DIR}watch.png"
#     img = "images/screenshots/specials.png"
#
#     # накладываем на скриншот маску с оттобранным цветом
#     # отбираем нужный цвет
#     button_color = [132, 179, 249]
#     low_color, height_color = create_low_and_height_color(button_color)
#     lower_color = np.array([*low_color])
#     upper_color = np.array([*height_color])
#     img = cv.imread(img)
#     target = cv.imread(target)
#     img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     mask = cv.inRange(img_hsv, lower_color, upper_color)
#     img_with_mask = cv.bitwise_and(img, img, mask=mask)
#     # img_with_mask = cv.imread(mask)
#     # result = cv.matchTemplate(img_with_mask, target, cv.TM_CCOEFF_NORMED)
#     method = cv.TM_CCORR_NORMED
#     result = cv.matchTemplate(img_with_mask, target, method)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
#
#     print(max_val)
#     threshold = 0.9
#     if max_val >= threshold:
#         # self.save_top_left_target_coords(max_loc)
#         logger.info("Target detected")
#     logger.error("Target not found")
#
#     # result = cv.bitwise_and(img, img, mask=mask)
#     # cv.imshow('Original', img)
#     # cv.imshow('Original2', img_hsv)
#     # cv.imshow('Mask', mask)
#     # cv.imshow('Result', result)
#     cv.imshow('Result', img_with_mask)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# ищем кнопку в этом скриншоте

# take_screenshot()
# button_color = [132, 179, 249]
# low_color, height_color = create_low_and_height_color(button_color)
# lower_color = np.array([*low_color])
# upper_color = np.array([*height_color])
# img = cv.imread(img)
# img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# mask = cv.inRange(img_hsv, lower_color, upper_color)
# result = cv.bitwise_and(img, img, mask=mask)

# Отображение результата
# cv.imshow('Original', img)
# cv.imshow('Mask', mask)
# cv.imshow('Result', result)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
# result = cv.matchTemplate(img, target, cv.TM_CCOEFF_NORMED)
# # cv2.TM_SQDIFF
# # cv2.TM_CCORR_NORMED
#
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
#
# # print(max_val)
# threshold = 0.9
# if max_val >= threshold:
#     # self.save_top_left_target_coords(max_loc)
#     logger.info("Target detected")
#     return True
# logger.error("Target not found")
# return False

# if img:
#     img_comp_obj = ImageComparison(target, img)
# else:
#     img_comp_obj = ImageComparison(target)
# if img_comp_obj.is_target_on_image():
#     img_comp_obj.tap_on_target()


def wait(sec: int):
    logger.info(f"Ждем {sec} секунд")
    time.sleep(sec)


def is_color_similar(pixel_color, target_color, tolerance=3):
    for i in range(3):
        # print(target_color[i])
        if target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance:
            continue
        return False
    return True


def get_coords_of_active_button():
    """"
    на текущем экране ищем активные кнопки
    """
    target = Targets.SpecialsMenu.button_watch
    # img_color = cv.imread('images/screenshots/ad.JPG')
    img_color = cv.imread(get_last_screenshot_path())
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    target_color = cv.imread(target)
    first_pixel_target_color = target_color[0, 0]
    target_grey = cv.imread(target, 0)
    w, h = target_grey.shape[::-1]

    res = cv.matchTemplate(img_gray, target_grey, cv.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    # print(loc)
    for pt in zip(*loc[::-1]):
        # print(pt[0], pt[1])
        x, y = pt[0], pt[1]
        pixel_color = img_color[y, x]
        # b, g, r = img_color[y, x]
        # print(b, g, r)
        # print(pixel_color)
        # blue = pixel_color[0]
        # green = pixel_color[1]
        # red = pixel_color[2]
        # print("RGB", red, green, blue, "\n")
        if is_color_similar(pixel_color, first_pixel_target_color):
            return x + w, y + h
    return None


def watch_and_close_ad(check_func):
    from pages.common import is_resume_on_screen, tap_button_resume, is_google_play_on_screen

    wait(5)  # wait for ad start
    logger.info("Начался просмотр рекламы\n")
    targets = Targets.for_closing_ads()

    start_time = time.time()
    while time.time() - start_time < 120:
        take_screenshot()
        print(targets)
        for target in targets:

            if is_target_on_screen(target):
                find_and_tap(target)
                wait(2)
                take_screenshot()
                break

        if is_resume_on_screen():  # значит крестик закрытия рекламы появляется до окончания времени
            tap_button_resume()
            wait(25)

        if check_func():
            logger.info("Реклама закончилась. Вернулись в меню.\n")
            break

        if is_google_play_on_screen():
            tap_system_button_back()
            wait(1)

    else:
        logger.error("За 90 секунд не получилось закрыть рекламу")
        stop()


class ImageComparison:

    def __init__(self, target_path, img_path=None, method=5, threshold=0.8):
        self.target_path = target_path
        self.target = cv.imread(target_path, 0)
        if not img_path:
            img_path = get_last_screenshot_path()
        self.img = cv.imread(img_path, 0)
        self.method: int = method
        self.threshold = threshold
        self.target_w: int = self.target.shape[1]
        self.target_h: int = self.target.shape[0]
        self.img_w: int = self.img.shape[1]
        self.img_h: int = self.img.shape[0]
        self.top_left_target_coords = None

    def save_top_left_target_coords(self, top_left):
        self.top_left_target_coords = top_left

    # def is_target_on_image(self, threshold=0.9, method=cv.TM_CCOEFF_NORMED):
    def is_target_on_image(self):
        logger.info(f"Ищем: {self.target_path}")
        result = cv.matchTemplate(self.img, self.target, self.method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # logger.info(f"Трэшхолд = {max_val}")
        if max_val >= self.threshold:
            if self.method == 5:
                self.save_top_left_target_coords(max_loc)
            elif self.method == 1:
                self.save_top_left_target_coords(min_loc)
            logger.info("Target detected")
            return True
        logger.info(f"Target not found. Value: {max_val}")
        return False

    def get_target_center_coords(self):
        # Х = коорд левой точки + половина ширины таргета
        x, y = self.top_left_target_coords
        # print(x + self.target_w / 2, y + self.target_h / 2)
        return x + self.target_w / 2, y + self.target_h / 2

    def tap_on_target(self):
        # self.show_found_object()
        x, y = self.get_target_center_coords()
        tap(x, y)

    def reduce_img_by_2_times(self):
        return cv.resize(self.img, (self.img_w // 2, self.img_h // 2))

    def show_found_object(self):
        bottom_right_target_coords = (
            self.top_left_target_coords[0] + self.target_w,
            self.top_left_target_coords[1] + self.target_h
        )
        cv.rectangle(self.img,
                     self.top_left_target_coords,
                     bottom_right_target_coords,
                     255, 2)

        resized_img = self.reduce_img_by_2_times()
        cv.imshow('Detected Point', resized_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

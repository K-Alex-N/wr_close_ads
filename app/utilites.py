import os
import subprocess
import time
from venv import logger

import cv2 as cv

from app.adb import tap
from app.commons import swipe_left
from settings import SCREENSHOTS_DIR, TARGETS_DIR


def take_screenshot():
    logger.info("Получаем скриншот")
    # with open(SCREENSHOT_PATH, "wb") as file:
    with open(f"{SCREENSHOTS_DIR}{time.time()}.png", "wb") as file:
        subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=file, check=True)


def get_last_screenshot_path():
    files = os.listdir(SCREENSHOTS_DIR)
    files = [f"{SCREENSHOTS_DIR}{file}" for file in files]
    last_screenshot_path = max(files, key=os.path.getctime)
    logger.info(last_screenshot_path)
    return last_screenshot_path
    # return "images/screenshots/1737918907.3581278.png"


# get_last_screenshot_path()


def is_object_on_screenshot(obj):
    pass


def tap_on_object():
    pass


def is_main_menu():
    target = f"{TARGETS_DIR}to_battle.png"
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        logger.info("Главное меню")
        return True
    logger.info("Не главное меню")
    return False


#     берем скриншот
#     проверяем есть ли крестик
#         затем жмем в то место где был обнаружен крестик
#     если крестика нето то проверяем наличие входа в главное меню
#         если ок то выходим


def build_targets_list(*targets):
    return [f"{TARGETS_DIR}{target}" for target in [*targets]]


def close_intro_ads():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    :return:
    """
    targets = build_targets_list(
        "close_first_windows.png",
        "ok.png",
        # "",
    )
    max_windows_to_close = 12
    max_screenshots_to_take_for_repeat_check = 2
    time_for_new_window_load_completion = 1.5
    time_to_wait_before_new_attempt = 0.5

    for i in range(max_windows_to_close):
        logger.info(f"Закрываем рекламу номер {i + 1}")
        time.sleep(time_for_new_window_load_completion)

        for k in range(max_screenshots_to_take_for_repeat_check):
            logger.info(f"Попытка номер:{k + 1}")
            take_screenshot()

            for target in targets:
                logger.info(f"Ищем: {target}")
                img_comp_obj = ImageComparison(target)
                if img_comp_obj.is_target_on_image():
                    img_comp_obj.tap_on_target()
                    break

            if is_main_menu():
                return

            time.sleep(time_to_wait_before_new_attempt)


def is_menu_special():
    target = f"{TARGETS_DIR}specials.png"
    logger.info(f"Ищем: {target}")
    img = "images/screenshots/specials.png"
    img_comp_obj = ImageComparison(target, img)
    if img_comp_obj.is_target_on_image():
        return True

    logger.error("Меню specials не открылось")


def enter_menu_special():
    target = f"{TARGETS_DIR}basket.png"
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    time.sleep(0.5)
    is_menu_special()
    # if not is_menu_special():
    #     logger.error("Меню specials не открылось")


def enter_menu_supply_center():
    pass


def check_if_menu_specials_displayed():
    number_of_attempts = 3
    time_to_wait_between_attempts = 2
    target = "images/specials.png"
    img = "images/screenshots/ad.JPG"

    for _ in range(number_of_attempts):
        # take_screenshot()
        img_comp_obj = ImageComparison(target, img)
        if img_comp_obj.is_target_on_image():
            print('OK - menu SPECIAL')
            return
        time.sleep(time_to_wait_between_attempts)
        continue
    assert "target with text 'SPECIAL' was not found"


# enter_in_
# check_if_menu_specials_displayed()

def open_page_2():
    pass


# def is_button_get_present():
#     target = f"{TARGETS_DIR}get.png"
#     img_comp_obj = ImageComparison(target)
#     if img_comp_obj.is_target_on_image():
#         return True
#     return False


def watch_and_close_ad():
    targets = build_targets_list(
        "close_ads/1.png",
        "close_ads/2.png",
        "close_ads/3.png",
        "close_ads/4.png",
        "close_ads/5.png",
    )
    start_time = time.time()
    while True:
        if time.time() - start_time > 90:
            logger.error("за 90 секунд не получилось закрыть рекламу")
            break

        take_screenshot()
        for target in targets:
            img_comp_obj = ImageComparison(target)
            if img_comp_obj.is_target_on_image():
                img_comp_obj.tap_on_target()

        if is_menu_special():
            break


        # ищем таргеты
        #     нажимаем
        #     проверяем что есть GET
        #         если есть то нажимаем
        #         если нет то повторяем - новый скриншот и так 90 раз




def detection_of_active_ad_button():
    """
    no-active button (in HSV) = 162 97 88
    active - 176 230 153

    я написал HSV но в Пэйнте было HSL.
    мб перепроверить цвет как советуют на этой страннице
    https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
    :return:
    """


def tap_button_watch():
    target = f"{TARGETS_DIR}watch.png"
    # low_color =
    # hight_color =

    take_screenshot()
    # cv.inRange(img, low_color, hight_color)
    img = "images/screenshots/specials.png"

    result = cv.matchTemplate(img, target, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # print(max_val)
    threshold = 0.9
    if max_val >= threshold:
        # self.save_top_left_target_coords(max_loc)
        logger.info("Target detected")
        return True
    logger.error("Target not found")
    return False

    # if img:
    #     img_comp_obj = ImageComparison(target, img)
    # else:
    #     img_comp_obj = ImageComparison(target)
    # if img_comp_obj.is_target_on_image():
    #     img_comp_obj.tap_on_target()


def tap_button_get():
    target = f"{TARGETS_DIR}get.png"
    for _ in range(2):
        take_screenshot()
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()
            return
    logger.error("button GET did not found")

def tap_button_ok():
    target = f"{TARGETS_DIR}ok.png"
    for _ in range(2):
        take_screenshot()
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()
            return
    logger.error("button OK did not found")

def watch_all_ads_on_the_page():
    while True:
        tap_button_watch()
        if not is_menu_special():
            watch_and_close_ad()
        tap_button_get()
        tap_button_ok()
        # swipe_left


            # check_if_menu_specials_displayed()
            # swipe_left(percentage=20)


class ImageComparison:

    def __init__(self, target_path, img_path=None):
        self.target = cv.imread(target_path, 0)
        if not img_path:
            img_path = get_last_screenshot_path()
        self.img = cv.imread(img_path, 0)
        self.target_w: int = self.target.shape[1]
        self.target_h: int = self.target.shape[0]
        self.img_w: int = self.img.shape[1]
        self.img_h: int = self.img.shape[0]
        self.top_left_target_coords = None

    def save_top_left_target_coords(self, top_left):
        self.top_left_target_coords = top_left

    # def is_target_on_image(self, threshold=0.9, method=cv.TM_CCOEFF_NORMED):
    def is_target_on_image(self):
        result = cv.matchTemplate(self.img, self.target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # print(max_val)
        threshold = 0.9
        if max_val >= threshold:
            self.save_top_left_target_coords(max_loc)
            logger.info("Target detected")
            return True
        logger.error("Target not found")
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

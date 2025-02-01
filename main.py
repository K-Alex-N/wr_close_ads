import subprocess
import time

import cv2
from numpy.ma.core import logical_or

from adb import start_app
from commons import swipe_left
from log.log import logger
from settings import SCREENSHOT_PATH, TARGETS_FOLDER
from utilites import ImageComparison


# def print_log(msg: str):
#     print()

def take_screenshot():
    logger.info("Получаем скриншот")
    with open(SCREENSHOT_PATH, "wb") as file:
        subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=file, check=True)


def close_window_if_possible():
    target_img_path = "images/targets/close_first_windows.png"
    target = cv2.imread(target_img_path, 0)

    pass


# пока просто закрыть первые рекламы!!!!!!!!!!!!!!!!!
# стартуем игру руками

# закрываем все предложения которые при старте


def is_object_on_screenshot(obj):

    pass


def tap_on_object():
    pass


def is_main_menu():
    pass

#     берем скриншот
#     проверяем есть ли крестик
#         затем жмем в то место где был обнаружен крестик
#     если крестика нето то проверяем наличие входа в главное меню
#         если ок то выходим

# for _ in range(20):
# for _ in range(1):
#     time.sleep(2)
#     # take_screenshot()
#     img_comp_obj = ImageComparison("images/close_first_windows.png")
#     if img_comp_obj.is_target_on_image():
#         print("detected !!!")
#         img_comp_obj.tap_on_target()
#     elif is_main_menu():
#         break
#     else:
#         print("ничего не найдено")
#         break
# else:
#     print("цикл повторился 20 раз. выход")


def close_intro_ads():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    :return:
    """
    target1 = "close_first_windows.png"
    target2 = "ok.png"
    targets = [f"{TARGETS_FOLDER}{target}" for target in [target1, target2]]
    # НЕСКОЛЬКО ТАРГЕТОВ!
    max_windows_to_close = 12
    max_screenshots_to_take_for_repeat_check = 2
    time_for_new_window_load_completion = 1.5
    time_to_wait_before_new_attempt = 0.5

    for i in range(max_windows_to_close):
        logger.info(f"Закрываем рекламу номер {i+1}")
        time.sleep(time_for_new_window_load_completion)

        for k in range(max_screenshots_to_take_for_repeat_check):
            logger.info(f"Попытка номер:{k+1}")
            take_screenshot()

            for target in targets:
                logger.info(f"Ищем: {target}")
                img_comp_obj = ImageComparison(target)
                if img_comp_obj.is_target_on_image():
                    img_comp_obj.tap_on_target()
                    break
                # else:
                #     continue
            time.sleep(time_to_wait_before_new_attempt)

        # проверка наличия кнопки Battle
        # закрыть его
        # выйти из интро



def check_if_menu_specials_displayed():
    number_of_attempts = 3
    time_to_wait_between_attempts = 2
    target = "images/SPECIALS.png"
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

def watch_and_close_ad():
    pass


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
    target = f"{TARGETS_FOLDER}watch.png"
    take_screenshot()
    # СТРАВНЕНИЕ ЦВЕТНЫХ ТАРГЕТОВ !!!!!!!!!!!!
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()


def tap_button_get():
    target = f"{TARGETS_FOLDER}get.png"
    take_screenshot()
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()


def tap_button_ok():
    target = f"{TARGETS_FOLDER}ok.png"
    take_screenshot()
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()


def watch_all_ads_on_the_page():
    while True:
        # if not is_menu_special():
        #     break
        tap_button_watch()
        # watch_and_close_ad()
        for _ in range(90):
            time.sleep(1)
            tap_button_get()
        tap_button_ok()

        target = "images/watch.png"
        take_screenshot()
        # img = "images/screenshots/ad22.JPG"
        # img_comp_obj = ImageComparison(target, img)
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()


            check_if_menu_specials_displayed()
            swipe_left(percentage=20)

start_app()
time.sleep(5)
close_intro_ads()

# watch_all_ads_on_the_page()
# open_page_2()
# watch_all_ads_on_the_page()
logger.info(">>>>>>>>>>>>ВСЁ>>>>>>>>>>>>")

# заходим в меню где реклама


# while True:
#     take_screenshot()
#     # check_content()
#     if is_ads_button_present():
#         take_coords_of_ads_button()
#         click_ads()
#         close_ads()
#     elif if_close_button_present:
#         close_window()
#     else:
#         print("END!!!")
#         break

import subprocess
import time

import cv2

from settings import SCREENSHOT_PATH
from utilites import ImageComparison


def take_screenshot():
    with open(SCREENSHOT_PATH, "wb") as file:
        subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=file, check=True)


def close_window_if_possible():
    target_img_path = "images/close_first_windows.png"
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
for _ in range(1):
    # take_screenshot()
    img_comp_obj = ImageComparison("images/close_first_windows.png")
    if img_comp_obj.is_target_on_image():
        print("detected !!!")
        tap_on_target()
#         time.sleep(3)
#     elif is_main_menu():
#         break
#     else:
#         print("ничего не найдено")
#         break
# else:
#     print("цикл повторился 20 раз. выход")


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

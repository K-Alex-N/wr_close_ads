import time

from app.utilites import take_screenshot, ImageComparison
from pages.base_page import is_target_on_screen, tap_button_get, is_button_get_on_screen
from pages.main_menu import open_menu_workshop_lev1
from pages.targets import Targets


def is_menu_workshop_lev1():
    target = Targets.MenuWorkshop.identifier_level_1
    return is_target_on_screen(target)

def is_menu_workshop_lev2():
    target = Targets.MenuWorkshop.identifier_level_2
    return is_target_on_screen(target)

def open_menu_workshop_lev2():
    # чтобы избавиться от кольцевых импортов то можно функцию прям в функцию передавать!!!
    take_screenshot()
    target = Targets.MainMenu.workshop_level_1_icon
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_workshop_lev2():
            break


def tap_all_get_buttons():
    while True:
        if is_button_get_on_screen():
            tap_button_get()
            break
    else:
        logger

def tap_all_repeat_buttons():
    pass


def start_all_works_in_workshop():
    open_menu_workshop_lev1()
    open_menu_workshop_lev2()
    tap_all_get_buttons()
    tap_all_repeat_buttons()
    # нажать на всеж Гет затем на всех Репер
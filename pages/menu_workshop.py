import time

from app.utilites import take_screenshot, ImageComparison
from pages.base_page import is_target_on_screen, tap_button_get, is_button_get_on_screen, find_and_tap, stop, \
    back_with_check, is_button_repeat_on_screen, tap_button_repeat
from pages.main_menu import open_menu_workshop_lev1, is_main_menu
from pages.targets import Targets
from log.log import logger


def is_menu_workshop_lev1():
    target = Targets.MenuWorkshop.identifier_level_1
    return is_target_on_screen(target)


def is_menu_workshop_lev2():
    target = Targets.MenuWorkshop.identifier_level_2
    return is_target_on_screen(target)


def open_menu_workshop_lev2():
    # чтобы избавиться от кольцевых импортов то можно функцию прям в функцию передавать!!!
    take_screenshot()
    target = Targets.MainMenu.menu_workshop_icon
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_workshop_lev2():
            break


def tap_all_buttons(check_func, act_func, success_msg):
    while True:
        if check_func():
            act_func()
            continue
        else:
            logger.info(success_msg)
            break


def tap_all_get_buttons():
    check_func = is_button_get_on_screen
    act_func = tap_button_get
    success_msg = "Все кнопки get нажаты"
    tap_all_buttons(check_func, act_func, success_msg)


def tap_all_repeat_buttons():
    check_func = is_button_repeat_on_screen
    act_func = tap_button_repeat
    success_msg = "Все кнопки repeat нажаты"
    tap_all_buttons(check_func, act_func, success_msg)


# def back_to_menu_workshop_level_1():
#     # может быть написать эту функцию а внутри уже back_with_check(is_menu_workshop_lev1)
#     # так же добавить каких нибудь сообщений
#     target = Targets.MenuWorkshop.back
#     find_and_tap(target)
#     # maybe todo fucntion check() - it will take screenshot and check with any function
#     # for example => check(is_menu_workshop_lev1)
#     take_screenshot()
#     if is_menu_workshop_lev1():
#         return
#     logger.error("Non menu workshop lev1")
#     stop()


def start_all_works_in_workshop():
    open_menu_workshop_lev1()
    open_menu_workshop_lev2()
    tap_all_get_buttons()
    tap_all_repeat_buttons()
    back_with_check(is_menu_workshop_lev1)
    back_with_check(is_main_menu)

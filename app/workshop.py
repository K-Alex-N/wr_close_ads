from app.utils import tap_all_buttons_on_screen, take_screenshot
from pages.common import is_button_get_on_screen, tap_button_get, is_button_repeat_on_screen, tap_button_repeat, \
    back_and_check
from pages.main_menu import open_menu_workshop_lev1, is_main_menu
from pages.menu_workshop import open_menu_workshop_lev2, is_menu_workshop_lev1


def tap_all_get_buttons():
    tap_all_buttons_on_screen(
        check_func=is_button_get_on_screen,
        act_func=tap_button_get,
        success_msg="Все кнопки get нажаты")


def tap_all_repeat_buttons():
    check_func = is_button_repeat_on_screen
    act_func = tap_button_repeat
    success_msg = "Все кнопки repeat нажаты"
    tap_all_buttons_on_screen(check_func, act_func, success_msg)


# main func
def start_all_works_in_workshop():
    take_screenshot()
    open_menu_workshop_lev1()
    open_menu_workshop_lev2()
    tap_all_get_buttons()
    tap_all_repeat_buttons()
    back_and_check(is_menu_workshop_lev1)
    back_and_check(is_main_menu)

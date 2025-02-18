from app.utils import watch_and_close_ad, wait
from app.screenshot import take_screenshot
from pages.common import back_and_check
from pages.main_menu import open_back_market_menu, is_main_menu
from pages.menu_black_market import is_button_open_for_free, tap_button_open_for_free, is_bronze_chest_menu, \
    is_black_market_menu


def watch_ad_in_black_market_menu():
    take_screenshot()
    open_back_market_menu()
    if is_button_open_for_free():
        tap_button_open_for_free()
        watch_and_close_ad(is_bronze_chest_menu)
        wait(12, "Ждем пока анимация закончится")  #
        take_screenshot()
        back_and_check(is_black_market_menu)
    back_and_check(is_main_menu)

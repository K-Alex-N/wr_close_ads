from app.utils import wait
from pages.base_page import is_target_on_screen, find_and_tap, back_and_check
from pages.main_menu import open_menu_supply_center, is_main_menu
from pages.targets import Targets


def is_menu_supply_center():
    target = Targets.SupplyCenterMenu.identifier
    return is_target_on_screen(target)


def get_first_free_supplies():
    target = Targets.SupplyCenterMenu.button_get_supplies
    if is_target_on_screen(target):
        find_and_tap(target)
        wait(11)  # ожидание пока рулетка крутится


def tap_button_get_more():
    target = Targets.SupplyCenterMenu.button_get_more
    find_and_tap(target)


def is_button_get_more_on_screen():
    target = Targets.SupplyCenterMenu.button_get_more
    return is_target_on_screen(target)


def watch_all_ads_in_supply_center_meny():
    open_menu_supply_center()
    get_first_free_supplies()
    while True:
        if not is_button_get_more_on_screen():
            break
        tap_button_get_more()
        watch_and_close_ad(is_menu_supply_center)
        wait(8)  # ожидание пока рулетка крутится
    back_and_check(is_main_menu)

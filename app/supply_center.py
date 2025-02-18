from app.utils import wait, watch_and_close_ad, is_target_on_screen, find_and_tap
from pages.common import back_and_check
from pages.main_menu import open_menu_supply_center, is_main_menu
from pages.menu_supply_center import is_button_get_more_on_screen, tap_button_get_more, is_menu_supply_center
from pages.targets import Targets


def get_first_free_supplies():
    target = Targets.SupplyCenterMenu.button_get_supplies
    if is_target_on_screen(target):
        find_and_tap(target)
        wait(11, "Ожидание пока рулетка крутится")


def watch_all_ads_in_supply_center_meny():
    open_menu_supply_center()
    get_first_free_supplies()
    while True:
        if not is_button_get_more_on_screen():
            break
        tap_button_get_more()
        watch_and_close_ad(is_menu_supply_center)
        wait(8, "Ожидание пока рулетка крутится")
    back_and_check(is_main_menu)

from app.utilites import ImageComparison, take_screenshot, wait
from pages.base_page import is_target_on_screen, find_and_tap, watch_and_close_ad, back_with_check
from pages.main_menu import open_menu_supply_center, is_main_menu
from pages.targets import Targets


def is_menu_supply_center():
    target = Targets.SupplyCenterMenu.identifier
    return is_target_on_screen(target)


# def back_to_main_menu():
#     target = Targets.SupplyCenterMenu.back_to_main_menu
#
#     for _ in range(2):
#         take_screenshot()
#         img_comp_obj = ImageComparison(target)
#         if img_comp_obj.is_target_on_image():
#             img_comp_obj.tap_on_target()
#
#         from pages.main_menu import is_main_menu
#         if is_main_menu():
#             return


def get_first_free_supplies():
    target = Targets.SupplyCenterMenu.button_get_supplies
    if is_target_on_screen(target):
        find_and_tap(target)
        wait(10)  # ожидание пока рулетка крутится


def tap_button_ad_in_supply_center():
    target = Targets.SupplyCenterMenu.button_get_more
    find_and_tap(target)


def is_button_ad():
    target = Targets.SupplyCenterMenu.button_get_more
    return is_target_on_screen(target)


def watch_all_ads_in_supply_center_meny():
    open_menu_supply_center()
    get_first_free_supplies()
    while True:
        if not is_button_ad():
            break
        tap_button_ad_in_supply_center()
        watch_and_close_ad(is_menu_supply_center)
        wait(5) # ожидание пока рулетка крутится
    back_with_check(is_main_menu)

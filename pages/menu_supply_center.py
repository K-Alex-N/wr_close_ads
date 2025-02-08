from app.app import watch_and_close_ad
from app.utilites import ImageComparison, take_screenshot
from log.log import logger
from pages.base_page import is_target_on_screen
from pages.main_menu import open_menu_supply_center
from pages.targets import Targets


def is_menu_supply_center():
    target = Targets.SupplyCenterMenu.identifier
    return is_target_on_screen(target)


def back_to_main_menu():
    target = Targets.SupplyCenterMenu.back_to_main_menu

    for _ in range(2):
        take_screenshot()
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()

        from pages.main_menu import is_main_menu
        if is_main_menu():
            return




def tap_button_ad_in_supply_center():
    target = Targets.SupplyCenterMenu.button_get_more
    find_and_tap()


def watch_all_ads_in_supply_center_meny():
    open_menu_supply_center()
    tap_button_ad_in_supply_center()
    watch_and_close_ad()

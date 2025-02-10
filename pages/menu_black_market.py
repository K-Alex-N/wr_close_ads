from app.utilites import ImageComparison, take_screenshot, wait
from pages.base_page import is_target_on_screen, find_and_tap, watch_and_close_ad
from pages.main_menu import open_back_market_menu
from pages.targets import Targets


def is_black_market_menu():
    target = Targets.BlackMarketMenu.identifier
    return is_target_on_screen(target)


def is_bronze_chest_menu():
    target = Targets.BlackMarketMenu.bronze_chest_menu
    return is_target_on_screen(target)

def back_to_black_market_menu():
    target = Targets.BlackMarketMenu.back_to_main_menu

    for _ in range(2):
        take_screenshot()
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()

        if is_black_market_menu():
            return

def back_to_main_menu():
    target = Targets.BlackMarketMenu.back_to_main_menu

    for _ in range(2):
        take_screenshot()
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()

        from pages.main_menu import is_main_menu
        if is_main_menu():
            return

def tap_button_open_for_free():
    target = Targets.BlackMarketMenu.button_open_for_free
    find_and_tap(target)



def watch_ad_in_black_market_menu():
    open_back_market_menu()
    tap_button_open_for_free()
    watch_and_close_ad(is_bronze_chest_menu)
    wait(5) # ждем пока анимация получения подарка закончится
    back_to_black_market_menu()
    back_to_main_menu()

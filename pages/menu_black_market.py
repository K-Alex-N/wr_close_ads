from app.utils import is_target_on_screen, find_and_tap
from pages.targets import Targets


def is_black_market_menu():
    target = Targets.BlackMarketMenu.identifier
    return is_target_on_screen(target)


def is_bronze_chest_menu():
    target = Targets.BlackMarketMenu.bronze_chest_menu
    return is_target_on_screen(target)


def is_button_open_for_free():
    target = Targets.BlackMarketMenu.button_open_for_free
    return is_target_on_screen(target)


def tap_button_open_for_free():
    target = Targets.BlackMarketMenu.button_open_for_free
    find_and_tap(target)

from app.utils import is_target_on_screen, find_tap_and_check
from pages.menu_black_market import is_black_market_menu
from pages.menu_specials import is_menu_special
from pages.menu_supply_center import is_menu_supply_center
from pages.menu_workshop import is_menu_workshop_lev1
from pages.targets import Targets


def is_main_menu():
    target = Targets.MainMenu.identifier
    return is_target_on_screen(target)


def is_menu_specials_icon_on_screen():
    target = Targets.MainMenu.menu_specials_icon
    return is_target_on_screen(target)


def open_menu_special():
    target = Targets.MainMenu.menu_specials_icon
    find_tap_and_check(target, is_menu_special)


def open_menu_supply_center():
    target = Targets.MainMenu.menu_supply_center_icon
    find_tap_and_check(target, is_menu_supply_center)


def open_back_market_menu():
    target = Targets.MainMenu.menu_black_market_icon
    find_tap_and_check(target, is_black_market_menu)


def open_menu_workshop_lev1():
    target = Targets.MainMenu.menu_workshop_icon
    find_tap_and_check(target, is_menu_workshop_lev1)

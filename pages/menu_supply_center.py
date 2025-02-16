from app.utils import is_target_on_screen, find_and_tap
from pages.targets import Targets


def is_menu_supply_center():
    target = Targets.SupplyCenterMenu.identifier
    return is_target_on_screen(target)


def is_button_get_more_on_screen():
    target = Targets.SupplyCenterMenu.button_get_more
    return is_target_on_screen(target)


def tap_button_get_more():
    target = Targets.SupplyCenterMenu.button_get_more
    find_and_tap(target)

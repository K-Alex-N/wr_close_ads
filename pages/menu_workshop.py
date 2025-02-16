from app.utils import is_target_on_screen, find_tap_and_check
from pages.targets import Targets


def is_menu_workshop_lev1():
    target = Targets.WorkshopMenu.identifier_level_1
    return is_target_on_screen(target)


def is_menu_workshop_lev2():
    target = Targets.WorkshopMenu.identifier_level_2
    return is_target_on_screen(target)


def open_menu_workshop_lev2():
    target = Targets.WorkshopMenu.workshop_level_2_icon
    find_tap_and_check(target, is_menu_workshop_lev2)

import sys


from app.utilites import take_screenshot, ImageComparison
from log.log import logger
from pages.base_page import is_target_on_screen
from pages.targets import Targets


def is_menu_special():
    target = Targets.MenuSpecials.identifier
    return is_target_on_screen(target)


def back_to_main_menu():
    for _ in range(2):
        take_screenshot()
        target = Targets.MenuSpecials.back_to_main_menu
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            img_comp_obj.tap_on_target()

        from pages.main_menu import is_main_menu
        if is_main_menu():
            return

    logger.error("Не получилось вернуться в главное меню")
    sys.exit()

import time

from app.utilites import ImageComparison, take_screenshot
from log.log import logger


from pages.targets import Targets


def is_main_menu():
    target = Targets.MainMenu.identifier
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        logger.info("Главное меню")
        return True
    logger.info("Не главное меню")
    return False

def is_menu_specials_icon_on_screen():
    from pages.base_page import is_target_on_screen
    # take_screenshot()
    target = Targets.MainMenu.menu_specials_icon
    if is_target_on_screen(target):
        return True

def open_menu_special():
    from pages.base_page import find_and_tap
    from pages.menu_specials import is_menu_special

    take_screenshot()
    target = Targets.MainMenu.menu_specials_icon
    find_and_tap(target)

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_special():
            break
    else:
        logger.error("Не получилось открыть меню specials")


def open_menu_supply_center():
    from pages.menu_supply_center import is_menu_supply_center

    take_screenshot()
    target = Targets.MainMenu.menu_supply_center_icon
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_supply_center():
            break
    else:
        logger.error("Не получилось открыть меню supply_center")

def open_back_market_menu():
    from pages.menu_black_market import is_black_market_menu
    # чтобы избавиться от кольцевых импортов то можно функцию прям в функцию передавать!!!
    take_screenshot()
    target = Targets.MainMenu.menu_black_market_icon
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_black_market_menu():
            logger.info(f"Зашли в black market меню\n")
            break
    else:
        logger.error(f"Не получилось открыть меню ")

def open_menu_workshop_lev1():
    from pages.menu_workshop import is_menu_workshop_lev1

    # чтобы избавиться от кольцевых импортов то можно функцию прям в функцию передавать!!!
    take_screenshot()
    target = Targets.MainMenu.menu_workshop_icon
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_workshop_lev1():
            break
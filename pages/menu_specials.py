from app.adb import tap, swipe_left
from app.utils import take_screenshot, get_coords_of_active_button
from log.log import logger

from pages.main_menu import open_menu_special, is_menu_specials_icon_on_screen, is_main_menu
from pages.targets import Targets


def is_menu_special():
    from pages.base_page import is_target_on_screen
    target = Targets.SpecialsMenu.identifier
    return is_target_on_screen(target)


def try_get_button_watch_coords():
    """"
    ищем кнопку просмотра рекламы на всех страницах в меню specials
    """
    # собрать все номера (а точнее номер 2 и 3)
    # если обнаружили 3 то ставим 3 цикла если 2 то два цикла

    from pages.base_page import back_and_check

    while True:
        coords = try_get_button_watch_coords_on_current_page()
        if coords:
            return coords

        back_and_check(is_main_menu)
        if not is_menu_specials_icon_on_screen():
            return None  # если иконки нет, то вся реклама просмотренна
        open_menu_special()

    # Возможно определение активной страницы по цвету кнопки

    # is_page_2_present()
    # switch_to_next_page()


def try_get_button_watch_coords_on_current_page():
    """
    Посмотреть рекламу на всей странице.
    Для этого смотрим рекламу на текущее странице,
    если не нашлось то сдвигаем экран влево и ищем еще раз
    """
    for _ in range(2):
        take_screenshot()
        coords = get_coords_of_active_button()
        if coords:
            return coords
        swipe_left()  # прокручиваем влево и повторяем поиск

    logger.info("Кнопка watch не найдена на странице")
    return None


# main function
def watch_all_ads_in_menu_specials():
    from pages.base_page import back_and_check
    from pages.base_page import is_button_get_on_screen
    from pages.base_page import watch_and_close_ad, tap_button_ok_and_check
    from pages.base_page import tap_button_get_and_check, is_button_ok_on_screen

    open_menu_special()

    while True:  # не известно сколько рекламы будет на странице и сколько страниц
        coords = try_get_button_watch_coords()
        if coords is None:
            break  # all ads are watched. Now we are in main menu
        tap(*coords)
        watch_and_close_ad(is_menu_special)
        if not is_button_get_on_screen():  # иногда после рекламы нет вознаграждения т.к. нужно посмотреть несколько реклам
            continue
        tap_button_get_and_check(is_button_ok_on_screen)
        tap_button_ok_and_check(is_menu_special)

    back_and_check(is_main_menu)

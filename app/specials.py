from app.adb import swipe_left, tap
from app.utils import get_coords_of_active_button, watch_and_close_ad
from app.screenshot import take_screenshot
from log.logger import logger
from pages.common import is_button_get_on_screen, tap_button_get_and_check, tap_button_ok_and_check, back_and_check, \
    is_button_ok_on_screen
from pages.main_menu import is_main_menu, is_menu_specials_icon_on_screen, open_menu_special
from pages.menu_specials import is_menu_special


def try_get_button_watch_coords():
    """"
    ищем кнопку просмотра рекламы на всех страницах в меню specials
    если не нашлось на текущей странице то выходим в главное меню и снова заходим
    """
    while True:
        coords = try_get_button_watch_coords_on_current_page()
        if coords:
            return coords

        back_and_check(is_main_menu)
        if not is_menu_specials_icon_on_screen():
            return None  # если иконки нет, то вся реклама просмотренна
        open_menu_special()


def try_get_button_watch_coords_on_current_page():
    """
    Посмотреть рекламу на всей странице.
    Сначала смотрим рекламу на текущей странице, затем "свайп" экрана влево и ищем еще раз
    """
    for _ in range(2):
        take_screenshot()
        coords = get_coords_of_active_button()
        if coords:
            return coords
        swipe_left()  # прокручиваем влево и повторяем поиск

    logger.info("Кнопка watch не найдена на странице")
    return None


def watch_all_ads_in_menu_specials():
    if not is_menu_specials_icon_on_screen():
        logger.info("Иконки меню specials нет.\n")
        return

    open_menu_special()

    while True:  # бесконечный цикл т.к. не известно сколько будет рекламы на странице и сколько будет страниц
        coords = try_get_button_watch_coords()
        if coords is None:
            break  # all ads are watched. Now we are in main menu
        tap(*coords)
        watch_and_close_ad(is_menu_special)
        if not is_button_get_on_screen():  # иногда после рекламы нет вознаграждения т.к. нужно посмотреть рекламу еще раз
            continue
        tap_button_get_and_check(is_button_ok_on_screen)
        tap_button_ok_and_check(is_menu_special)

    back_and_check(is_main_menu)
    logger.info("Просмотр рекламы в меню specials закончен.\n")

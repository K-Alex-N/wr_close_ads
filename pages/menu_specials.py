import sys

from app.adb import tap, swipe_left
from app.utilites import take_screenshot, get_coords_of_active_button
from log.log import logger


from pages.main_menu import open_menu_special, is_menu_specials_icon_on_screen, is_main_menu
from pages.targets import Targets


def is_menu_special():
    from pages.base_page import is_target_on_screen
    target = Targets.SpecialsMenu.identifier
    return is_target_on_screen(target)



# def back_to_main_menu():
#     for _ in range(2):
#         take_screenshot()
#         target = Targets.MenuSpecials.back_to_main_menu
#         img_comp_obj = ImageComparison(target)
#         if img_comp_obj.is_target_on_image():
#             img_comp_obj.tap_on_target()
#
#         from pages.main_menu import is_main_menu
#         if is_main_menu():
#             return
#
#     logger.error("Не получилось вернуться в главное меню")
#     sys.exit()


def try_get_button_watch_coords():
    """"
    ищем кнопку просмотра рекламы на всех страницах в меню specials
    """
    # собрать все номера (а точнее номер 2 и 3)
    # если обнаружили 3 то ставим 3 цикла если 2 то два цикла

    while True:
        coords = try_get_button_watch_coords_on_current_page()
        if coords:
            return coords

        # back_to_main_menu()
        back_with_check(is_main_menu)
        if not is_menu_specials_icon_on_screen():
            return None
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
        swipe_left()

    logger.info("Кнопки watch не найдено на страницу")
    return None

# main function
def watch_all_ads_in_menu_specials():
    from pages.base_page import back_with_check
    from pages.base_page import tap_button_ok, tap_button_get
    from pages.base_page import is_button_get_on_screen
    from pages.base_page import watch_and_close_ad

    open_menu_special()

    while True:  # не известно сколько рекламы будет на странице и сколько страниц
        coords = try_get_button_watch_coords()
        if coords is None:
            break  # all ads are watched. Now we are in main menu
        tap(*coords)
        # wait(1) # wait for
        watch_and_close_ad(is_menu_special)
        if not is_button_get_on_screen():  # иногда после рекламы нет вознаграждения т.к. нужно посмотреть несколько реклам
            continue
        tap_button_get()
        take_screenshot()
        tap_button_ok()

    back_with_check(is_main_menu)

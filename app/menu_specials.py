import time

from app.adb import tap_back, swipe_left, tap
from app.main_menu import is_main_menu
from app.utilites import take_screenshot, ImageComparison, build_targets_list, tap_button_get, tap_button_watch, \
    tap_button_ok, take_all_targets_for_closing_ads
from log.log import logger
from settings import TARGETS_DIR


def is_menu_special():
    target = f"{TARGETS_DIR}specials.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        return True


def open_menu_special():
    target = f"{TARGETS_DIR}basket.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    for _ in range(3):
        time.sleep(0.5)
        take_screenshot()
        if is_menu_special():
            break
    else:
        logger.error("Не найдено меню specials")


def back_to_main_menu():
    target = f"{TARGETS_DIR}to_hangar.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    # if not is_main_menu():
    #     return


def get_coords_of_active_button():
    tolerance=3
    get_all_findings()

    pass


def get_button_watch_coords_on_current_page():
    """
    Действие нужно повторить 2 раза.
    Вначале ищем на первой части экрана
    Затем сдвигаем экран влево и ищем еще раз

    :return:
    """
    for _ in range(2):
        coords = get_coords_of_active_button()
        if coords:
            return coords
        swipe_left()

    return None


def get_button_watch_coords():
    coords = get_button_watch_coords_on_current_page()
    if coords:
        return coords

    back_to_main_menu()
    open_menu_special()  # либо мб сразу на главном меню искать иконку
    if not is_menu_special():
        return None

    # start recursion
    get_button_watch_coords()


def watch_all_ads_in_menu_specials():
    open_menu_special()
    while True:
        coords = get_button_watch_coords()
        if not coords:
            break  # we are in main menu
        tap(*coords)
        watch_and_close_ad()
        tap_button_get()
        tap_button_ok()

        # # если не нажимали на выход и время на рекламу вышло, а мы все еще в режиме просмотра
        # if ad_mode and (not tap_exit_ad) and ((time.time() - start_time_ad) > timeout_ad):
        #     printLog("timeout_ad")
        #     height, width, _ = img_rgb.shape
        #     tap_screen(width - 50, 50)  # жмем в ту область, где он должен быть

        # как еще определить что вся реклама просмотрена???

        # to do it every time
        # выйти в главное меню
        # есть ли кнопка-корзинки?
        # если ее нет то вся реклама просмотрена и выходим из бесконечного цыкла
        # если есть то заходим снова

        # check_if_menu_specials_displayed()


def is_google_play():
    target = f"{TARGETS_DIR}google_play.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        return True


def watch_and_close_ad():
    targets = take_all_targets_for_closing_ads()
    start_time = time.time()
    while True:
        tm = time.time() - start_time
        print(tm)
        if tm > 90:
            logger.error("за 90 секунд не получилось закрыть рекламу")
            break

        take_screenshot()
        for target in targets:
            img_comp_obj = ImageComparison(target)
            if img_comp_obj.is_target_on_image():
                img_comp_obj.tap_on_target()

        if is_google_play():
            tap_back()

        if is_menu_special():
            break

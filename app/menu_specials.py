import time

from app.adb import tap_back, swipe_left
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


def watch_all_ads_on_the_page():
    while True:
        tap_button_watch()
        time.sleep(3)
        if not is_menu_special():
            watch_and_close_ad()
        tap_button_get()
        tap_button_ok()
        swipe_left()

        # выйти в главное меню и проверить наличие кнопки-корзинки. если ее нет то вся реклама просмотрена

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
        if time.time() - start_time > 90:
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


def switch_to_page_2():
    pass


def watch_all_ads_in_menu_specials():
    # open_menu_special()
    # watch_all_ads_on_the_page()
    # switch_to_page_2()
    watch_all_ads_on_the_page()

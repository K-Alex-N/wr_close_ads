import sys
import time
import cv2 as cv
import numpy as np

from app.adb import tap_back, swipe_left, tap
from app.utilites import ImageComparison, take_screenshot, get_last_screenshot_path, tap_button_get, tap_button_ok, wait
from log.log import logger
from pages.base_page import is_button_get_on_screen
from pages.main_menu import is_main_menu, open_menu_special, is_menu_specials_icon_on_screen
from pages.menu_specials import is_menu_special, back_to_main_menu
from pages.targets import Targets


def is_color_similar(pixel_color, target_color, tolerance=3):
    for i in range(3):
        # print(target_color[i])
        if target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance:
            continue
        return False
    return True


def get_coords_of_active_button():
    """"
    на текущем экране ищем активные кнопки
    """
    target = Targets.MenuSpecials.button_watch
    # img_color = cv.imread('images/screenshots/ad.JPG')
    img_color = cv.imread(get_last_screenshot_path())
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    target_color = cv.imread(target)
    first_pixel_target_color = target_color[0, 0]
    target_grey = cv.imread(target, 0)
    w, h = target_grey.shape[::-1]

    res = cv.matchTemplate(img_gray, target_grey, cv.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    # print(loc)
    for pt in zip(*loc[::-1]):
        # print(pt[0], pt[1])
        x, y = pt[0], pt[1]
        pixel_color = img_color[y, x]
        # b, g, r = img_color[y, x]
        # print(b, g, r)
        # print(pixel_color)
        # blue = pixel_color[0]
        # green = pixel_color[1]
        # red = pixel_color[2]
        # print("RGB", red, green, blue, "\n")
        if is_color_similar(pixel_color, first_pixel_target_color):
            return x + w, y + h
    return None


def get_button_watch_coords_on_current_page():
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


def get_button_watch_coords():
    """"
    ищем кнопку просмотра рекламы на всех страницах в меню specials
    """
    # собрать все номера (а точнее номер 2 и 3)
    # если обнаружили 3 то ставим 3 цикла если 2 то два цикла


    while True:
        coords = get_button_watch_coords_on_current_page()
        if coords:
            return coords

        back_to_main_menu()
        if not is_menu_specials_icon_on_screen():
            return None
        open_menu_special()

    # todo Возможно определение активной страницы по цвету кнопки

    # is_page_2_present()
    # switch_to_next_page()


    # наверное нужно создать что то типа tap_menu_special - что означает что нет проверки
    # if not is_menu_special():
    #     return None

    # УБРАТЬ РЕКУРСИЮ или как то правильно ее закрывать
    # get_button_watch_coords() # start recursion. it's watch ads on all pages.


def watch_all_ads_in_menu_specials():
    open_menu_special()
    # определение по номеру предложения сделать
    while True:
        coords = get_button_watch_coords()
        # print(coords)
        if coords is None:
            break  # all ads are watched. Now we are in main menu
        tap(*coords)
        # wait(1) # wait for
        watch_and_close_ad()
        if not is_button_get_on_screen():
            continue
        # иногда после рекламы нет вознаграждения т.к. нужно посмотреть несколько реклам
        tap_button_get()
        tap_button_ok()

    back_to_main_menu()

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
    target = Targets.google_play
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        return True


def watch_and_close_ad():
    logger.info("Начался просмотр рекламы")
    targets = Targets.for_closing_ads()
    start_time = time.time()
    while True:
        take_screenshot()
        for target in targets:
            img_comp_obj = ImageComparison(target, threshold=0.8)
            if img_comp_obj.is_target_on_image():
                img_comp_obj.tap_on_target()
                break

        if is_google_play():
            tap_back()

        if is_menu_special():
            logger.info("Реклама закончилась. Мы в меню specials.")
            break

        ad_time = time.time() - start_time
        logger.info(f"реклама длится: {ad_time} секунд")
        if ad_time > 90:
            logger.error("за 90 секунд не получилось закрыть рекламу")
            stop()
            break


def is_loader_present():
    target = Targets.loader
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        logger.info("Обнаружен loader")
        return True


def close_intro():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    """
    targets = Targets.build_targets_list(
        "yes.png",  # так как можно попасть в зацыкливание если появляется one-time offer
        "close_first_windows.png",
        "ok.png",
    )
    max_windows_to_close = 15
    max_retry = 3
    time_for_new_window_load_completion = 1
    # time_to_wait_before_new_attempt = 0.5

    for i in range(max_windows_to_close):
        logger.info(f"Закрываем интро номер {i + 1}")
        wait(time_for_new_window_load_completion)

        for j in range(max_retry):
            logger.info(f"Попытка номер:{j + 1}")
            take_screenshot()

            if is_loader_present():
                logger.info("Попалась иконка загрузки")
                continue

            for target in targets:
                logger.info(f"Ищем: {target}")
                img_comp_obj = ImageComparison(target)
                if img_comp_obj.is_target_on_image():
                    img_comp_obj.tap_on_target()
                    break

            if is_main_menu():
                return

            # # щелканье в то место где должен быть крестик только в том случае если не не шли главное меню и не нашли крести. А может быть вооюще убрать
            # # пробуем просто нажать в то место где крестик
            # tap(2356, 56)

        else:
            logger.info(f"Не получилось закрыть интро номер {i + 1}")
            # wait(time_to_wait_before_new_attempt)

    else:
        stop()


def stop():
    logger.error("Остановка программы")
    sys.exit()

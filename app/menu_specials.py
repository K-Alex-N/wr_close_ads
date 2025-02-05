import time
import cv2 as cv
import numpy as np

from app.adb import tap_back, swipe_left, tap
from app.main_menu import is_main_menu
from app.utilites import take_screenshot, ImageComparison, build_targets_list, tap_button_get, tap_button_watch, \
    tap_button_ok, take_all_targets_for_closing_ads, get_last_screenshot_path
from log.log import logger
from settings import TARGETS_DIR


def is_menu_special():
    target = f"{TARGETS_DIR}specials.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        return True


def open_menu_special():
    take_screenshot()
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
    take_screenshot()
    target = f"{TARGETS_DIR}to_hangar.png"
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        img_comp_obj.tap_on_target()

    # if not is_main_menu():
    #     return


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

    # img_color = cv.imread('images/screenshots/ad.JPG')
    img_color = cv.imread(get_last_screenshot_path())
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    target_color = cv.imread('images/targets/watch.png')
    first_pixel_target_color = target_color[0, 0]
    target_grey = cv.imread('images/targets/watch.png', 0)
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
            print(coords)
            return coords
        swipe_left()

    return None


def get_button_watch_coords():
    """"
    ищем кнопку просмотра рекламы на всех страницах в меню specials
    """
    coords = get_button_watch_coords_on_current_page()
    if coords:
        return coords

    back_to_main_menu()
    open_menu_special()  # либо мб сразу на главном меню искать иконку
    if not is_menu_special():
        return None

    get_button_watch_coords() # start recursion. it's watch ads on all pages.


def watch_all_ads_in_menu_specials():
    open_menu_special()
    while True:
        coords = get_button_watch_coords()
        print(coords)
        if coords is None:
            break  # all ads are watched. Now we are in main menu
        tap(*coords)
        time.sleep(1)
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

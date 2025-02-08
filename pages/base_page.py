import cv2 as cv
import numpy as np

from app.adb import tap
from app.experiments.create_white_black_img import img_path
from app.utilites import ImageComparison, take_screenshot, get_last_screenshot_path
from log.log import logger
from pages.targets import Targets


def is_target_on_screen(target, number_of_attempts = 2):
    for _ in range(number_of_attempts):
        img_comp_obj = ImageComparison(target)
        if img_comp_obj.is_target_on_image():
            return True
        take_screenshot()

    logger.info(f"Target {target} did not found after {number_of_attempts} attempts")
    return False

def find_and_tap(target_path, img_path=None, method=5, threshold=0.87, number_of_attempts=2):
    target =  cv.imread(target_path, 0)

    for attempt in range(number_of_attempts):
        #debug
        if img_path:
            img = cv.imread(img_path, 0)
        else:
            img = cv.imread(get_last_screenshot_path(), 0)
        logger.info(f"Ищем: {target_path}")
        result = cv.matchTemplate(img, target, method)
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            logger.info("Target detected")
            break

        logger.info(f"{attempt+1} attempt")
        take_screenshot()

    else:
        logger.info(f"Target not found. {number_of_attempts} attempts. Value: {max_val}")
        return

    x, y = max_loc
    h, w = target.shape
    tap(x + w / 2, y + h / 2)

    # if is_target_on_screen(target):


def is_button_get_on_screen():
    target = Targets.button_get
    return is_target_on_screen(target)
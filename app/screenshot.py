import os
import subprocess
import time

from log.log import logger
from settings import SCREENSHOTS_DIR

last_screenshot = None


def take_screenshot():
    logger.info("Получаем новый скриншот")
    screenshot_name = os.path.join(SCREENSHOTS_DIR, f"{time.time()}.png")
    with open(screenshot_name, "wb") as file:
        subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=file, check=True)

    global last_screenshot
    last_screenshot = screenshot_name


def get_last_screenshot_path():
    if last_screenshot is not None:
        logger.info(f"Берем скриншот: {last_screenshot}")
        return last_screenshot

    take_screenshot()
    get_last_screenshot_path()

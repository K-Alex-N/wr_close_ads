import os
import time

WORK_DIR = os.path.abspath(os.curdir)
SCREENSHOT_FOLDER = "images/screenshots/"
TARGETS_FOLDER = "images/targets/"
SCREENSHOT_PATH = os.path.join(WORK_DIR, f"{SCREENSHOT_FOLDER}{time.time()}.png")

# SCREENSHOT_PATH = os.path.join(WORK_DIR, 'images', 'screenshot.png')

# print(SCREENSHOT_PATH)
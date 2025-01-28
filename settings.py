import os
import time

WORK_DIR = os.path.abspath(os.curdir)

SCREENSHOT_PATH = os.path.join(WORK_DIR, f"images/screenshots/{time.time()}.png")
# SCREENSHOT_PATH = os.path.join(WORK_DIR, 'images', 'screenshot.png')

# print(SCREENSHOT_PATH)
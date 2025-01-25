import os
import subprocess

from settings import SCREENSHOT_PATH

# os.system(r"adb exec-out screencap -p > C:\Users\akurochkin\PycharmProjects\wr_close_ads\screen.png")

# img = subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=subprocess.PIPE).stdout  # получаем файл
subprocess.run(['adb', 'exec-out', 'screencap', '-p', '>', {SCREENSHOT_PATH}])
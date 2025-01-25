import os
import subprocess

from settings import SCREENSHOT_PATH

# os.system(r"adb exec-out screencap -p > C:\Users\akurochkin\PycharmProjects\wr_close_ads\screen.png")

# img = subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=subprocess.PIPE).stdout  # получаем файл
# subprocess.run(['adb', 'exec-out', 'screencap', '-p', '>', {SCREENSHOT_PATH}], stdout=file, check=True)
# subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=SCREENSHOT_PATH, check=True)
output_path="images/screenshot.png"
with open(output_path, "wb") as file:
    subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=file, check=True)


# import subprocess
#
# def capture_screenshot(output_path="screenshot.png"):
#     try:
#         # Команда для создания скриншота на устройстве
#         subprocess.run(["adb", "shell", "screencap", "/sdcard/screenshot.png"], check=True)
#
#         # Команда для копирования скриншота на компьютер
#         subprocess.run(["adb", "pull", "/sdcard/screenshot.png", output_path], check=True)
#
#         # Опционально: удаление скриншота с устройства
#         subprocess.run(["adb", "shell", "rm", "/sdcard/screenshot.png"], check=True)
#
#         print(f"Скриншот сохранён как {output_path}")
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка при выполнении команды ADB: {e}")
#
# # Запуск функции
# capture_screenshot("my_screenshot.png")

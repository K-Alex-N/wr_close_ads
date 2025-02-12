# img_raw = subprocess.run(['C:\\platform-tools\\adb.exe', 'exec-out', 'screencap',
#                           '-p'], stdout=subprocess.PIPE).stdout  # получаем файл


import subprocess
from typing import Union

from PIL.ImageChops import offset

from log.log import logger


def execute(command: Union[list, str]) -> subprocess.CompletedProcess:
    command = command.split()
    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    if result.returncode != 0:
        logger.error(f'Failed execute command: {result.stderr}')

    return result


# def start_adb_connection():
#     logger.info("Запуск соединения с телефоном")
#     execute("adb tcpip 5555")
#     execute("adb connect 192.168.1.46:5555")

def start_adb_connection():
    print("Open on your smartphone > Wireless debugging > Pair device with pairing code")
    port = input("Enter port number")
    print(port)
    addr = f"192.168.1.46:{port}"
    print(addr)
    msg = f"adb pair {addr}"
    # execute(f"adb pair {addr}")
    print(msg)
    execute(msg)
    pwd = input("Enter 6 digits password")
    print(pwd)
    execute(pwd)


def start_app():
    logger.info("Запуск игры")
    execute("adb shell am start -n com.pixonic.wwr/com.unity3d.player.UnityPlayerActivity")


def tap(x, y):
    logger.info(f"Нажимаем на {x} {y}")
    execute(f"adb shell input tap {x} {y}")


def tap_system_button_back():
    execute("adb shell input keyevent KEYCODE_BACK")


# sound ---------------

def set_media_sound_volume(volume: int):
    execute(f"adb shell cmd media_session volume --show --stream 3 --set {volume}")


def turn_off_media_sound():
    logger.info("Устанавливаем громкость музыки на ноль")
    set_media_sound_volume(0)


def set_max_media_sound():
    logger.info("Устанавливаем максимальный уровень громкости музыки")
    set_media_sound_volume(15)


# swipe ---------------

def swipe(x1, y1, x2, y2, duration=500):
    execute(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")


def swipe_left():
    # offset
    x1, x2 = 1500, 1000
    y1 = y2 = 500
    swipe(x1, y1, x2, y2)

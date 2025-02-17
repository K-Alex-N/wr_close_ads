# img_raw = subprocess.run(['C:\\platform-tools\\adb.exe', 'exec-out', 'screencap',
#                           '-p'], stdout=subprocess.PIPE).stdout  # получаем файл


import subprocess
from typing import Union

from log.log import logger


def execute(command: Union[list, str]) -> subprocess.CompletedProcess:
    command = command.split()
    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    if result.returncode != 0:
        logger.error(f'Failed execute command: {result.stderr}')
        from app.utils import stop
        stop()

    return result


def start_adb_connection():
    print("Open on your smartphone > Wireless debugging > Pair device with pairing code")
    port = input("Enter port number: ")
    pwd = input("Enter 6 digits password: ")
    addr = f"192.168.1.46:{port} {pwd}"
    msg = f"adb pair {addr}"
    execute(msg)
    print(msg)
    print("Wait for 'Wireless debugging connected' message appear")
    input("After tap any button")


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


def set_medium_media_sound_level():
    logger.info("Устанавливаем средний уровень громкости музыки")
    set_media_sound_volume(7)


# swipe ---------------


def swipe(x1, y1, x2, y2, duration=500):
    execute(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")


def swipe_left():
    # offset
    x1, x2 = 1500, 1000
    y1 = y2 = 500
    swipe(x1, y1, x2, y2)

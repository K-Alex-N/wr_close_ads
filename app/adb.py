# tap back
# subprocess.run(['C:\\platform-tools\\adb.exe', 'shell', 'input keyevent 4'])

# img_raw = subprocess.run(['C:\\platform-tools\\adb.exe', 'exec-out', 'screencap',
#                           '-p'], stdout=subprocess.PIPE).stdout  # получаем файл


import subprocess
from typing import Union

from log.log import logger


def execute(command: Union[list, str]) -> subprocess.CompletedProcess:
    if isinstance(command, str):
        command = command.split()

    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    if result.returncode != 0:
        logger.error(f'Failed execute command: {result.stderr}')

    return result

def set_media_sound_volume(volume: int):
    execute(f"adb shell cmd media_session volume --show --stream 3 --set {volume}")

def turn_off_media_sound():
    logger.info("Устанавливаем громкость музыки на ноль")
    set_media_sound_volume(0)

def set_max_media_sound():
    logger.info("Устанавливаем максимальный уровень громкости музыки")
    set_media_sound_volume(15)

def tap(x, y):
    logger.info(f"Нажимаем на {x} {y}")
    execute(f"adb shell input tap {x} {y}")

def start_app():
    logger.info("Запуск игры")
    execute("adb shell am start -n com.pixonic.wwr/com.unity3d.player.UnityPlayerActivity")


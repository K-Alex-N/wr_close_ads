# tap back
# subprocess.run(['C:\\platform-tools\\adb.exe', 'shell', 'input keyevent 4'])


# os.system(r"adb exec-out screencap -p > C:\screen.png")

# img_raw = subprocess.run(['C:\\platform-tools\\adb.exe', 'exec-out', 'screencap',
#                           '-p'], stdout=subprocess.PIPE).stdout  # получаем файл


import subprocess
from typing import Union


def execute(command: Union[list, str]) -> subprocess.CompletedProcess:
    if isinstance(command, str):
        command = command.split(' ')

    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    if result.returncode != 0:
        print(f'Failed execute command: {result.stderr}')

    return result


def tap(x, y):
    execute(f"adb shell input tap {x} {y}")

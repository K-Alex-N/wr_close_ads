from app.utils import wait, stop, ImageComparison, is_target_on_screen, find_and_tap
from app.screenshot import take_screenshot
from log.log import logger
from pages.common import is_loader_on_screen
from pages.main_menu import is_main_menu
from pages.targets import Targets


def close_intro():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    """
    targets = Targets.intro_targets
    max_windows_to_close = 15
    max_retry = 3
    time_for_new_window_load_completion = 1
    # time_to_wait_before_new_attempt = 0.5

    for i in range(max_windows_to_close):
        logger.info(f"Закрываем интро номер {i + 1}")
        wait(time_for_new_window_load_completion)

        for j in range(max_retry):
            logger.info(f"Попытка номер:{j + 1}")
            take_screenshot()

            if is_loader_on_screen():
                logger.info("Попалась иконка загрузки")
                continue

            for target in targets:
                if is_target_on_screen(target):
                    find_and_tap(target)
                    break

            if is_main_menu():
                logger.info(f"Интро закончилось. Зашли в главное меню\n")
                return

        else:
            logger.info(f"Не получилось закрыть интро номер {i + 1}")
            # wait(time_to_wait_before_new_attempt)

    else:
        stop()

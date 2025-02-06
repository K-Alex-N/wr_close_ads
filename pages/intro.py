import time

from app.adb import tap
from pages.main_menu import is_main_menu
from app.utilites import ImageComparison, build_targets_list, take_screenshot
from log.log import logger
from pages.targets import Targets


def is_loader_present():
    target = Targets.loader
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        logger.info("Обнаружен loader")
        return True


def close_intro():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    """
    targets = build_targets_list(
        "yes.png",  # так как можно попасть в зацыкливание если появляется one-time offer
        "close_first_windows.png",
        "ok.png",
        # "",
    )
    max_windows_to_close = 12
    max_retry = 2
    time_for_new_window_load_completion = 1.5
    time_to_wait_before_new_attempt = 0.5

    for i in range(max_windows_to_close):
        logger.info(f"Закрываем интро номер {i + 1}")
        time.sleep(time_for_new_window_load_completion)

        for k in range(max_retry):
            logger.info(f"Попытка номер:{k + 1}")
            take_screenshot()

            if is_loader_present():
                time.sleep(0.5)
                continue

            for target in targets:
                logger.info(f"Ищем: {target}")
                img_comp_obj = ImageComparison(target)
                if img_comp_obj.is_target_on_image():
                    img_comp_obj.tap_on_target()
                    break

            if is_main_menu():
                return

            # пробуем просто нажать в то место где крестик
            tap(2356, 56)

            time.sleep(time_to_wait_before_new_attempt)

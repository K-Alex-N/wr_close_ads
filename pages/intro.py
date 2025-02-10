from app.utilites import wait, take_screenshot, stop, ImageComparison
from log.log import logger
from pages.base_page import is_loader_on_screen
from pages.main_menu import is_main_menu
from pages.targets import Targets


def close_intro():
    """
    max_windows_to_close - во время интро может быть очень много предложений к покупке
    """
    targets = Targets.build_targets_list(
        "yes.png",  # так как можно попасть в зацыкливание если появляется one-time offer
        "close_first_windows.png",
        "ok.png",
    )
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
                logger.info(f"Ищем: {target}")
                img_comp_obj = ImageComparison(target)
                if img_comp_obj.is_target_on_image():
                    img_comp_obj.tap_on_target()
                    break

            if is_main_menu():
                return

            # # щелканье в то место где должен быть крестик только в том случае если не не шли главное меню и не нашли крести. А может быть вооюще убрать
            # # пробуем просто нажать в то место где крестик
            # tap(2356, 56)

        else:
            logger.info(f"Не получилось закрыть интро номер {i + 1}")
            # wait(time_to_wait_before_new_attempt)

    else:
        stop()
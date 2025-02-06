from app.utilites import ImageComparison
from log.log import logger
from pages.targets import Targets


def is_main_menu():
    target = Targets.MainMenu.identifier
    logger.info(f"Ищем: {target}")
    img_comp_obj = ImageComparison(target)
    if img_comp_obj.is_target_on_image():
        logger.info("Главное меню")
        return True
    logger.info("Не главное меню")
    return False

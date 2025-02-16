from app.utils import is_target_on_screen
from pages.targets import Targets


def is_menu_special():
    target = Targets.SpecialsMenu.identifier
    return is_target_on_screen(target)

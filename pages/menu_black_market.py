from app.utilites import ImageComparison
from pages.base_page import is_target_on_screen
from pages.targets import Targets


def is_black_market_menu():
    target = Targets.BlackMarketMenu.identifier
    return is_target_on_screen(target)


import os

from settings import TARGETS_DIR


# WORK_DIR = os.path.dirname(os.path.abspath(os.curdir))
# TARGETS_DIR = os.path.join(WORK_DIR, "images", "targets")


class Targets:
    loader = os.path.join(TARGETS_DIR, "loader.png")

    button_ok = os.path.join(TARGETS_DIR, "ok.png")
    button_get = os.path.join(TARGETS_DIR, "get.png")
    button_repeat = os.path.join(TARGETS_DIR, "repeat.png")

    back_buttons = [
        os.path.join(TARGETS_DIR, "back.png"),
        os.path.join(TARGETS_DIR, "to_hangar.png"),
    ]

    google_play_targets = [
        os.path.join(TARGETS_DIR, "google_play.png"),
        os.path.join(TARGETS_DIR, "google_play2.png"),
        os.path.join(TARGETS_DIR, "google_play3.png"),
    ]

    intro_targets = [
        os.path.join(TARGETS_DIR, "yes.png"), # должно быть первым чтобы не попасть в зацыкливание при one-time offer
        os.path.join(TARGETS_DIR, "close_first_windows.png"),
        button_ok,
    ]

    class MainMenu:
        MAIN_MENU_DIR = os.path.join(TARGETS_DIR, "menu", "main")

        identifier = os.path.join(MAIN_MENU_DIR, "to_battle.png")
        menu_specials_icon = os.path.join(MAIN_MENU_DIR, "basket.png")
        menu_supply_center_icon = os.path.join(MAIN_MENU_DIR, "supply_center_icon.png")
        menu_black_market_icon = os.path.join(MAIN_MENU_DIR, "black_market_menu_icon.png")
        menu_workshop_icon = os.path.join(MAIN_MENU_DIR, "workshop_level_1_icon.png")

    class SpecialsMenu:
        SPECIALS_DIR = os.path.join(TARGETS_DIR, "menu", "specials")

        identifier = os.path.join(SPECIALS_DIR, "specials.png")
        # back_to_main_menu = os.path.join(TARGETS_DIR, to_hangar.png"
        button_watch = os.path.join(SPECIALS_DIR, "watch.png")

    class SupplyCenterMenu:
        SUPPLY_CENTER_DIR = os.path.join(TARGETS_DIR, "menu", "supply_center")

        identifier = os.path.join(SUPPLY_CENTER_DIR, "supply_center.png")
        # back_to_main_menu = os.path.join(TARGETS_DIR, back.png"
        button_get_supplies = os.path.join(SUPPLY_CENTER_DIR, "get_supplies.png")
        button_get_more = os.path.join(SUPPLY_CENTER_DIR, "get_more.png")
        # open_ad  =   get more

    class BlackMarketMenu:
        BLACK_MARKET_DIR = os.path.join(TARGETS_DIR, "menu", "black_market")

        identifier = os.path.join(BLACK_MARKET_DIR, "black_market.png")
        button_open_for_free = os.path.join(BLACK_MARKET_DIR, "open_for_free.png")
        # open_ad  =   open_for_free
        bronze_chest_menu = os.path.join(BLACK_MARKET_DIR, "bronze_chest.png")

    class WorkshopMenu:
        WORKSHOP_DIR = os.path.join(TARGETS_DIR, "menu", "workshop")

        identifier_level_1 = os.path.join(WORKSHOP_DIR, "robots.png")
        identifier_level_2 = os.path.join(WORKSHOP_DIR, "workshop.png")
        workshop_level_2_icon = os.path.join(WORKSHOP_DIR, "workshop_level_2_icon.png")

    @staticmethod
    def for_closing_ads():
        targets = os.listdir(os.path.join(TARGETS_DIR, "close_ads"))
        return [os.path.join(TARGETS_DIR, "close_ads", target) for target in [*targets]]

import os

from settings import TARGETS_DIR


class Targets:
    loader = f"{TARGETS_DIR}loader.png"
    google_play_targets = [
        f"{TARGETS_DIR}google_play.png",
        f"{TARGETS_DIR}google_play2.png",
        f"{TARGETS_DIR}google_play3.png",
    ]
    button_ok = f"{TARGETS_DIR}ok.png"
    button_get = f"{TARGETS_DIR}get.png"
    button_repeat = f"{TARGETS_DIR}repeat.png"

    class MainMenu:
        identifier = f"{TARGETS_DIR}to_battle.png"
        menu_specials_icon = f"{TARGETS_DIR}basket.png"
        menu_supply_center_icon = f"{TARGETS_DIR}supply_center_icon.png"
        black_market_menu = f"{TARGETS_DIR}black_market_menu_icon.png"
        workshop_level_1_icon = f"{TARGETS_DIR}workshop_level_1_icon.png"

    class MenuSpecials:
        identifier = f"{TARGETS_DIR}specials.png"
        back_to_main_menu = f"{TARGETS_DIR}to_hangar.png"
        button_watch = f"{TARGETS_DIR}watch.png"

    class SupplyCenterMenu:
        identifier = f"{TARGETS_DIR}supply_center.png"
        back_to_main_menu = f"{TARGETS_DIR}back.png"
        button_get_supplies = f"{TARGETS_DIR}get_supplies.png"
        button_get_more = f"{TARGETS_DIR}get_more.png"
        # open_ad  =   get more

    class BlackMarketMenu:
        identifier = f"{TARGETS_DIR}black_market.png"
        button_open_for_free = f"{TARGETS_DIR}open_for_free.png"
        # open_ad  =   open_for_free
        back_to_main_menu = f"{TARGETS_DIR}back.png"
        bronze_chest_menu = f"{TARGETS_DIR}bronze_chest.png"

    class MenuWorkshop:
        identifier_level_1 = f"{TARGETS_DIR}robots.png"
        identifier_level_2 = f"{TARGETS_DIR}workshop.png"
        workshop_level_2_icon = f"{TARGETS_DIR}workshop_level_2_icon.png"
        back_to_main_menu = f"{TARGETS_DIR}back.png"

    @staticmethod
    def for_closing_ads():
        targets_list = os.listdir(f"{TARGETS_DIR}close_ads")
        return [f"{TARGETS_DIR}close_ads/{target}" for target in [*targets_list]]

    @staticmethod
    def build_targets_list(*targets):
        return [f"{TARGETS_DIR}{target}" for target in [*targets]]

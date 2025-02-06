import os

from settings import TARGETS_DIR


class Targets:
    loader = f"{TARGETS_DIR}loader.png"
    google_play = f"{TARGETS_DIR}google_play.png"
    button_ok = f"{TARGETS_DIR}ok.png"
    button_get = f"{TARGETS_DIR}get.png"

    class MainMenu:
        identifier = f"{TARGETS_DIR}to_battle.png"
        menu_specials_icon = f"{TARGETS_DIR}basket.png"

    class MenuSpecials:
        identifier = f"{TARGETS_DIR}specials.png"
        back_to_main_menu = f"{TARGETS_DIR}to_hangar.png"
        button_watch = f"{TARGETS_DIR}watch.png"

    @staticmethod
    def for_closing_ads():
        targets_list = os.listdir(f"{TARGETS_DIR}close_ads")
        return [f"{TARGETS_DIR}close_ads/{target}" for target in [*targets_list]]

    @staticmethod
    def build_targets_list(*targets):
        return [f"{TARGETS_DIR}{target}" for target in [*targets]]

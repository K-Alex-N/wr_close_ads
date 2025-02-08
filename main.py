import time

from app.adb import start_app, turn_off_media_sound, start_adb_connection
from app.app import close_intro, watch_all_ads_in_menu_specials
from app.experiments.create_white_black_img import img_path
from app.utilites import wait

from log.log import logger
from pages.base_page import find_and_tap
from pages.menu_supply_center import watch_all_ads_in_supply_center_meny
from pages.targets import Targets

# start_adb_connection()

start_app()
turn_off_media_sound()
wait(15)
close_intro()
watch_all_ads_in_menu_specials()
#
# watch_all_ads_in_supply_center_meny()
# set_max_media_sound()
logger.info(">>>>>>>>>>>>ВСЁ>>>>>>>>>>>>")

target = Targets.
# find_and_tap(target, img_path)
find_and_tap(target)


# tap_button_watch()

# tap_button_watch2()  # разные методы потестить

# start_time = time.time()
# for _ in range(100):
#     get_coords_of_active_button()
# print(get_coords_of_active_button())
# print(time.time() - start_time)
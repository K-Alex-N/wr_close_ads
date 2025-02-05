import time

from app.adb import start_app, turn_off_media_sound, set_max_media_sound, tap_back, swipe_left, start_adb_connection
from app.intro import close_intro
from app.menu_specials import watch_all_ads_in_menu_specials, get_coords_of_active_button
from app.utilites import take_all_targets_for_closing_ads
from log.log import logger

# start_adb_connection()

# start_app()
# turn_off_media_sound()
# time.sleep(15)
# close_intro()
watch_all_ads_in_menu_specials()

# enter_menu_supply_center()
# set_max_media_sound()
logger.info(">>>>>>>>>>>>ВСЁ>>>>>>>>>>>>")

# tap_button_watch()

# tap_button_watch2()  # разные методы потестить

# start_time = time.time()
# for _ in range(100):
#     get_coords_of_active_button()
# print(get_coords_of_active_button())
# print(time.time() - start_time)
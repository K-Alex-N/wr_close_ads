import time

from app.adb import start_app, turn_off_media_sound, start_adb_connection
from app.utilites import wait

from log.log import logger
from pages.base_page import find_and_tap, is_google_play
from pages.menu_black_market import watch_ad_in_black_market_menu
from pages.menu_specials import watch_all_ads_in_menu_specials
from pages.menu_supply_center import watch_all_ads_in_supply_center_meny
from pages.targets import Targets

# start_adb_connection()

# start_app()
# turn_off_media_sound()
# wait(15)
# close_intro()
watch_ad_in_black_market_menu()
watch_all_ads_in_menu_specials()
watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
watch_all_ads_in_supply_center_meny()
watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
# set_max_media_sound()
logger.info(">>>>>>>>>>>>УСПЕШНО ОКОНЧЕНО<<<<<<<<<<<<")


# target = Targets.
# find_and_tap(target, img_path)
# find_and_tap(target)


# tap_button_watch()

# tap_button_watch2()  # разные методы потестить

# start_time = time.time()
# for _ in range(100):
#     get_coords_of_active_button()
# print(get_coords_of_active_button())
# print(time.time() - start_time)
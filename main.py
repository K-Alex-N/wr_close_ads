import time

from app.adb import start_app, turn_off_media_sound, start_adb_connection
from app.utilites import wait

from log.log import logger
from pages.base_page import find_and_tap, is_google_play
from pages.intro import close_intro
from pages.menu_black_market import watch_ad_in_black_market_menu
from pages.menu_specials import watch_all_ads_in_menu_specials
from pages.menu_supply_center import watch_all_ads_in_supply_center_meny
from pages.menu_workshop import start_all_works_in_workshop
from pages.targets import Targets
from settings import *


# adb pair 192.168.1.46:44087
# start_adb_connection()  # todo как проверить что соединение установлено? adb devices?
# start_app()
# turn_off_media_sound()
# wait(15)
# close_intro()
# watch_ad_in_black_market_menu()
# watch_all_ads_in_menu_specials()
# watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
# watch_all_ads_in_supply_center_meny()
# watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
start_all_works_in_workshop()

# set_max_media_sound()
logger.info(">>>УСПЕШНО ОКОНЧЕНО<<<")



# start_time = time.time()
# for _ in range(100):
#     get_coords_of_active_button()
# print(get_coords_of_active_button())
# print(time.time() - start_time)
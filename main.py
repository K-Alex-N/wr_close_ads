from app.adb import start_adb_connection, start_app, turn_off_media_sound
from app.black_market import watch_ad_in_black_market_menu
from app.intro import close_intro
from app.utils import wait
from log.log import logger

from pages.menu_specials import watch_all_ads_in_menu_specials
from pages.menu_supply_center import watch_all_ads_in_supply_center_meny
from pages.menu_workshop import start_all_works_in_workshop


# start_adb_connection()
# start_app()
turn_off_media_sound()
# wait(15)
close_intro()
# watch_ad_in_black_market_menu()
# watch_all_ads_in_menu_specials()
# watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
# watch_all_ads_in_supply_center_meny()
# watch_ad_in_black_market_menu() # добавляем снова т.к. через 30 секунд он восстанавливается
# start_all_works_in_workshop()

# set_max_media_sound()
logger.info(">>>УСПЕШНО ОКОНЧЕНО<<<")



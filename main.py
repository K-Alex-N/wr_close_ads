import time

from app.adb import start_app
from log.log import logger
from app.utilites import close_intro_ads, watch_all_ads_on_the_page, open_page_2, enter_menu_special, \
    enter_menu_supply_center, build_targets_list, is_menu_special, tap_button_watch

# start_app()
# # уменьшить громкость
# time.sleep(15)
# close_intro_ads()
# enter_menu_special()
# watch_all_ads_on_the_page()
# open_page_2()
# watch_all_ads_on_the_page()
# enter_menu_supply_center()
logger.info(">>>>>>>>>>>>ВСЁ>>>>>>>>>>>>")
# включить звук на всю на телефоне

tap_button_watch()

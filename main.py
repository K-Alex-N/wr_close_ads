from log.logger import logger
from app.adb import pair_device_via_wifi, start_app, turn_off_media_sound, set_medium_media_sound_level, execute
from app.utils import wait
from app.black_market import watch_ad_in_black_market_menu
from app.intro import close_intro
from app.specials import watch_all_ads_in_menu_specials
from app.supply_center import watch_all_ads_in_supply_center_meny
from app.workshop import start_all_works_in_workshop

pair_device_via_wifi()
start_app()
turn_off_media_sound()
wait(15, "Ждем загрузку игры")
close_intro()
watch_all_ads_in_menu_specials()
watch_ad_in_black_market_menu()
watch_all_ads_in_supply_center_meny()
watch_ad_in_black_market_menu()  # добавляем снова т.к. через 30 секунд приз восстанавливается
start_all_works_in_workshop()
set_medium_media_sound_level()
logger.info(">>>END<<<")




from app.utils import is_target_on_screen, find_and_tap, find_tap_and_check
from log.log import logger
from pages.targets import Targets


# is_*_on_screen


def is_button_get_on_screen() -> bool:
    target = Targets.button_get
    return is_target_on_screen(target)


def is_button_ok_on_screen() -> bool:
    target = Targets.button_ok
    return is_target_on_screen(target)


def is_button_repeat_on_screen() -> bool:
    target = Targets.button_repeat
    return is_target_on_screen(target)


def is_resume_on_screen() -> bool:
    target = Targets.button_resume
    return is_target_on_screen(target)


def is_loader_on_screen() -> bool:
    target = Targets.loader
    return is_target_on_screen(target)


def is_google_play_on_screen() -> bool or None:
    for target in Targets.google_play_targets:
        if is_target_on_screen(target):
            return True


# find_and_tap


def tap_button_get():
    target = Targets.button_get
    find_and_tap(target)


def tap_button_ok():
    target = Targets.button_ok
    find_and_tap(target)


def tap_button_repeat():
    target = Targets.button_repeat
    find_and_tap(target)


def tap_button_resume():
    target = Targets.button_resume
    find_and_tap(target)


# find, tap and check


def tap_button_get_and_check(check_func):
    target = Targets.button_get
    find_tap_and_check(target, check_func)


def tap_button_ok_and_check(check_func):
    target = Targets.button_ok
    find_tap_and_check(target, check_func)


# miscellaneous


def back_and_check(check_func, to_take_new_screenshot=False):
    from app.utils import take_screenshot, stop, wait

    if to_take_new_screenshot:
        take_screenshot()

    targets = Targets.back_buttons
    for target in targets:
        if is_target_on_screen(target):
            find_and_tap(target)
            wait(1)
            take_screenshot()
            break

    if check_func():
        logger.info("Удачно вернулись в предыдущее меню\n")
    else:
        logger.error("Не получилось вернутся в предыдущее меню")
        stop()


import cv2

def take_screenshot():
    # КОД ОТ ИИ
    # pip     install    adb    - а зачем это?????????????????

    from adb import Client
    import cv2
    import numpy as np

    # Подключение к устройству
    client = Client(host='127.0.0.1', port=5037)
    device = client.device("emulator-5554")  # Замените на имя вашего устройства

    # Сделать скриншот
    result = device.screencap()

    # Преобразовать данные скриншота в изображение
    image = cv2.imdecode(np.frombuffer(result, np.uint8), cv2.IMREAD_COLOR)

    # Показать скриншот (необязательно)
    cv2.imshow("Screenshot", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Сохранить скриншот
    cv2.imwrite("screenshot.png", image)

    pass


def close_window_if_possible():
    target_img_path = "images/close_first_windows.png"
    target = cv2.imread(target_img_path, 0)

    pass

# пока просто закрыть первые рекламы!!!!!!!!!!!!!!!!!
# стартуем игру руками

while True:
    take_screenshot()
    # check_content()
    if is_ads_button_present():
        take_coords_of_ads_button()
        click_ads()
        close_ads()
    elif if_close_button_present:
        close_window()
    else:
        print("END!!!")
        break


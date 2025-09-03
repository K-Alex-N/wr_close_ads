
# import cv2
# import numpy as np
#
# # Загрузка изображений
# img = cv2.imread('image.jpg')
# template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Метод сопоставления (выберите подходящий)
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#
# # Выбор метода
# method = eval(methods[0])
#
# # Выполнение сопоставления
# res = cv2.matchTemplate(img_gray, template, method)
#
# # Поиск минимального (для SQDIFF и SQDIFF_NORMED) или максимального значения (для других методов)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
# # Отображение результатов
# if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#     top_left = min_loc
# else:
#     top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
# cv2.rectangle(img,top_left, bottom_right, 255, 2)
# cv2.imshow('Detected Point',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
import numpy as np

img1 = "images/screenshots/1737918907.3581278.png"
# img2 = "images/123.png"
img2 = "images/close_first_windows.png"

# Загрузка изображений
img = cv2.imread(img1)
template = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Метод сопоставления (выберите подходящий)
method = cv2.TM_CCOEFF_NORMED

# Выполнение сопоставления
res = cv2.matchTemplate(img_gray, template, method)

# Поиск минимального (для SQDIFF и SQDIFF_NORMED) или максимального значения (для других методов)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Отображение результатов
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
bottom_right = (top_left[0], top_left[1])
cv2.rectangle(img,top_left, bottom_right, 255, 2)
cv2.imshow('Detected Point',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img1 = "images/screenshots/1737918907.3581278.png"
# img2 = "images/123.png"
img2 = "images/close_first_windows.png"

# Загрузка изображения и шаблона
image = cv2.imread(img1, 0)
template = cv2.imread(img2, 0)

# Сопоставление шаблонов
# result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
# print(result)
# cv2.imshow('Detected', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Установка порога для определения совпадений
threshold = 0.8
loc = np.where(result >= threshold)
print(loc)
print(*loc)
print(*loc[::-1])

# Вывод координат найденных совпадений
for pt in zip(*loc[::-1]):
    print(f"Найдено совпадение в координатах: {pt}")

# Рисование прямоугольников вокруг найденных совпадений
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

# # Показ результата
# cv2.imshow('Detected', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
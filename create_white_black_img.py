import cv2

img_path ="images/raw/2025-01-23 21-43-06.JPG"

img = cv2.imread(img_path, 0)
# img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
red = 147
green = 74
blue = 249

BGR_value = np.uint8([[[blue,green,red]]])
HSV_value = cv.cvtColor(BGR_value, cv.COLOR_BGR2HSV)
print(HSV_value)

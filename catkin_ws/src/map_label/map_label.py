import numpy as np
import cv2

img = cv2.imread('map.jpg')

cv2.circle(img,(157, 124), 3, (0, 0, 255), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

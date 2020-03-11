import numpy as np
import cv2

height = 217
map_c_x = int((-1.6777+4.681169)/0.05)
map_c_y = height - int((0.0255478+3.636700)/0.05)

img = cv2.imread('passion.jpg')
cv2.circle(img,(map_c_x, map_c_y), 3, (0, 0, 255), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

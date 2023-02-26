import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.imshow("Blank", blank)

# this will not create a white image
# white_blank = np.ones((500, 500), dtype='uint8')
# cv2.imshow('white blank', white_blank)

img = cv2.imread("../samples/chosen_death.png")
cv2.imshow("Cat", img)

# 1. Paint the image a certain colour

blank[:] = 121, 195, 110

cv2.imshow("green", blank)

blank[200:300, 300:360] = 99, 95, 110
cv2.imshow("with square", blank)


cv2.waitKey(0)

import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.imshow("Blank", blank)

# 1. Paint the image a certain colour

blank[:] = 121, 195, 110

cv2.imshow("green", blank)

blank[200:300, 300:360] = 99, 95, 110
cv2.imshow("with square", blank)

# 2. Draw a Rectangle

blank = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(blank, (0, 0), (100, 100), (255, 0, 0), thickness=2)
cv2.imshow("rectangle", blank)


blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.rectangle(blank, (0, 0), (500, 100), (255, 0, 0), thickness=-1)
cv2.imshow("long rectangle", blank)


blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.rectangle(
    blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 0, 0), thickness=-1
)
cv2.imshow("square", blank)


cv2.waitKey(0)

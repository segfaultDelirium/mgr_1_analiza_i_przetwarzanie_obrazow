import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized", resized)

flip_vertically = cv2.flip(img, 0)
cv2.imshow("flip_vertically", flip_vertically)


flip_horizontally = cv2.flip(img, 1)
cv2.imshow("flip_horizontally", flip_horizontally)
#
flip_vertically_and_horizontally = cv2.flip(img, -1)
cv2.imshow("flip_vertically_and_horizontally", flip_vertically_and_horizontally)

cv2.waitKey(0)

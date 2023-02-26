import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

cropped = img[200:400, 300: 360]
cv2.imshow('cropped saruman', cropped)

cropped2 = img[0: img.shape[0] // 2, 0: img.shape[1] // 2]
cv2.imshow('cropped saruman 2', cropped2)


cv2.waitKey(0)

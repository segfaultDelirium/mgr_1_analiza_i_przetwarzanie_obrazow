import cv2
import numpy as np
import os

print(os.getcwd())

# # img = cv.imread('../chosen_death.png')
# img = cv.imread('../samples/korvin_bingo2.jpg')
# img = cv.imread('../samples/chosen_death.png')
img = cv2.imread("../samples/wallpaper.jpg")

cv2.imshow("cat", img)
cv2.waitKey(0)

print(np.arange(1, 10))

print(os.get_exec_path())

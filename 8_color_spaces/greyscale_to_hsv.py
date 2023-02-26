import cv2
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("greyscale saruman", grayscale)

bgr = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)
cv2.imshow("greyscale but BGR", bgr)


# BGR to HSV
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

#
plt.show()

cv2.waitKey(0)

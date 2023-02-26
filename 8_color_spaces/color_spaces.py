import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("greyscale saruman", grayscale)


# BGR to HSV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

# BGR to LAB

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)

plt.imshow(img)
plt.show()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

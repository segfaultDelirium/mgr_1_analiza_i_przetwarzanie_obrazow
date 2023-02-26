import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale saruman", grayscale)

blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('blurred', blur)

canny = cv2.Canny(blur, 125, 175)
# canny = cv2.Canny(grayscale, 125, 175)
cv2.imshow("canny saruman", canny)

result, threshold = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("threshold", threshold)

# contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE)
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# contours, hierarchies = cv2.findContours(
#     threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
# )
print(f"{len(contours)} contours found!")


blank = np.zeros(img.shape, dtype="uint8")
cv2.imshow("blank", blank)


cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow("contours drawn", blank)

cv2.waitKey(0)

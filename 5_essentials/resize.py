import cv2

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

resized = cv2.resize(img, (500, 500))

resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)

cv2.imshow("saruman resized", resized)


cv2.waitKey(0)

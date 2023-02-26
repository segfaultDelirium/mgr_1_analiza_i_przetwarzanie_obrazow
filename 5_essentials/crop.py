import cv2

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

cropped = img[50:200, 200:400]

cv2.imshow("cropped", cropped)


cv2.waitKey(0)

import cv2

img = cv2.imread('../samples/chosen_death.png')

cv2.imshow('saruman', img)

# blurred = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
blurred = cv2.GaussianBlur(img, (31, 31), cv2.BORDER_DEFAULT)

cv2.imshow('blurred saruman', blurred)

cv2.waitKey(0)

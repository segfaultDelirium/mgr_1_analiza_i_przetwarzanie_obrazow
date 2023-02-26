import cv2

img = cv2.imread('../samples/chosen_death.png')

cv2.imshow('saruman', img)

blurred = cv2.GaussianBlur(img, (31, 31), cv2.BORDER_DEFAULT)

cv2.imshow('blurred saruman', blurred)

# canny = cv2.Canny(img, 125, 175)

canny = cv2.Canny(img, 125, 125)

cv2.imshow('canny saruman', canny)

blurred = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
blurred_canny = cv2.Canny(blurred, 125, 125)
cv2.imshow('blurred canny saruman', blurred_canny)

cv2.waitKey(0)

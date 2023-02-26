import cv2

img = cv2.imread('../samples/chosen_death.png')

cv2.imshow('saruman', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('greyscale saruman', gray)

cv2.waitKey(0)

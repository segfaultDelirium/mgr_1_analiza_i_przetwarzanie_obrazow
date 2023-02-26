
import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)


blank = np.zeros((800, 800), dtype='uint8')
cv2.imshow('blank', blank)

rectangle = cv2.rectangle(blank.copy(), (380, 380), (570, 570), 255, -1)
cv2.imshow('rectangle', rectangle)

circle = cv2.circle(blank.copy(), (300, 400), 300, 255, -1)
cv2.imshow('circle', circle)


bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise AND between circle and rectangle', bitwise_and)


bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise OR between circle and rectangle', bitwise_or)

bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('bitwise XOR between circle and rectangle', bitwise_xor)

cv2.waitKey(0)

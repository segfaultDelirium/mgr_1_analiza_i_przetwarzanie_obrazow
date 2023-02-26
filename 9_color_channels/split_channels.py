import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)

b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("red", r)
cv2.imshow("green", g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merged = cv2.merge([b, g, r])
cv2.imshow("merged image", merged)

merged_switched_colors = cv2.merge([r, b, g])
cv2.imshow("switched colors", merged_switched_colors)


# create red, green and blue images with monocolor
# blank, _, _ = cv2.split(np.zeros(img.shape, dtype="uint8"))
blank = np.zeros(img.shape[:2], dtype="uint8")
print(blank)

red_monochannel = cv2.merge([blank, blank, r])
cv2.imshow('red_monochannel', red_monochannel)

green_monochannel = cv2.merge([blank, g, blank])
cv2.imshow('green_monochannel', green_monochannel)

blue_monochannel = cv2.merge([b, blank, blank])
cv2.imshow('blue_monochannel', blue_monochannel)
cv2.waitKey(0)

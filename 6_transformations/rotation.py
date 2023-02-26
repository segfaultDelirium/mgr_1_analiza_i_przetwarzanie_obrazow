import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)


def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]
    if rotation_point is None:
        rotation_point = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotation_matrix, dimensions)


rotated = rotate(img, 30)

cv2.imshow("rotated saruman", rotated)

rotated_clockwise = rotate(img, -30)
cv2.imshow("rotated clockwise saruman", rotated_clockwise)


rotated_back = rotate(rotated, -30)
cv2.imshow("saruman rotated and then rotated back", rotated_back)


cv2.waitKey(0)

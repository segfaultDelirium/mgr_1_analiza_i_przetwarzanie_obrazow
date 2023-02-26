import cv2
import numpy as np

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)


# -x means translation to left
# -y means translation up
def translate(img, x, y):
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, translation_matrix, dimensions)


translated = translate(img, 100, 100)
cv2.imshow("translated image right and down", translated)

translated = translate(img, -1 * img.shape[1] // 2, img.shape[0] // 2)
cv2.imshow("translated image left and down", translated)

cv2.waitKey(0)

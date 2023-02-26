import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.imshow("Blank", blank)

cv2.line(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 200, 140),
    thickness=3,
)


cv2.line(
    blank,
    (blank.shape[1], 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 200, 140),
    thickness=3,
)


cv2.imshow("Line", blank)
cv2.waitKey(0)

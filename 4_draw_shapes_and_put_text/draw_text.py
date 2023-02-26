import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.imshow("Blank", blank)

cv2.putText(
    blank,
    "hello, my name is jeff",
    (0, blank.shape[0] // 2),
    cv2.FONT_HERSHEY_COMPLEX,
    1.0,
    (0, 255, 0),
    2,
)

cv2.imshow("Text", blank)
cv2.waitKey(0)

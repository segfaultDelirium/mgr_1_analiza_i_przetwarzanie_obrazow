import cv2

img = cv2.imread("../samples/chosen_death.png")

cv2.imshow("saruman", img)


averaging_blur = cv2.blur(img, (3, 3))
# averaging_blur = cv2.blur(img, (33, 33))
cv2.imshow('averaging_blur', averaging_blur)


gaussian_blur = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('gaussian_blur', gaussian_blur)

median_blur = cv2.medianBlur(img, 3)
cv2.imshow('median_blur', median_blur)

# bilateral blurring
bilateral_blur = cv2.bilateralFilter(img, 15, 25, 25)
cv2.imshow('bilateral_blur', bilateral_blur)

cv2.waitKey(0)

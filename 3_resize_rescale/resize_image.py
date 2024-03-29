import cv2


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


img = cv2.imread('../samples/chosen_death.png')

cv2.imshow('Cat', img)

cv2.imshow('Resized image', rescaleFrame(img, 0.2))

cv2.waitKey()


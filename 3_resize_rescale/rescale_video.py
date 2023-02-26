import cv2


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


capture = cv2.VideoCapture("../samples/audi_a4.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, 0.3)

    cv2.imshow("Video", frame)
    cv2.imshow("Video resized", frame_resize)
    if cv2.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv2.destroyAllWindows()





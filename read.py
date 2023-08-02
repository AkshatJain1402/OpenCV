import cv2 as cv
img = cv.imread('Images/cat.jpeg')

# *// 0 means infinite time


def changeRes(width, height):
    # *// only live video not for video file
    capture.set(3, width)  # 3 is width
    capture.set(4, height)  # 4 is height


def rescaleFrame(frame, scale=1):
    width = int(frame.shape[1] * scale)  # frame.shape[1] is width
    height = int(frame.shape[0] * scale)  # frame.shape[0] is height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Video/cat.mp4')
img_resized = rescaleFrame(img)
cv.imshow('Image Resized', img_resized)
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):  # if letter d is pressed then break the video
        break

capture.release()
cv.destroyAllWindows()

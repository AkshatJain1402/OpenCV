import numpy as np
import cv2 as cv
img = cv.imread('Images/cat.jpeg')

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# blur the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# (7,7) is the kernel size that is the amount of blur
# cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
# to reduce the edges apply blur
# cascade image is the image with edges
# 125 is the threshold 1 and 175 is the threshold 2
# cv.imshow('Canny Edges', canny)


# dilating the image
dilated = cv.dilate(img, (7, 7), iterations=3)
# dilate means to make the edges thicker
# iterations is the amount of time we want to dilate the image
# cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (7, 7), iterations=32)
# erode means to make the edges thinner
# cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.INTER_AREA is the interpolation method , interpolation is the way of resizing the image when we wwant to smaller the image
# cv.INTER_LINEAR is the interpolation method , interpolation is the way of resizing the image when we wwant to larger the image
# cubic is slower than linear but gives better results


# cv.INTER_CUBIC is the interpolation method , interpolation is the way of resizing the image
# ignoring the aspect ratio
# cv.imshow('Resized', resized)

# cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)
def translate(img, x, y):
    transMAt = np.float32([[1, 0, x], [0, 1, y]])
    # the list first is the width and second is the height
    # 1 is the width and 0 is the height transMAt is the matrix that is used to translate the image

    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMAt, dimensions)
    # warpAffine is the function to translate the image that takes the image, the matrix and the dimensions of the image


# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
# the image was shifted 100 pixels to the right and 100 pixels down

# rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    # [:2] means only height and width
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    # if the rotation point is not given then the rotation point is the centre of the image
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    # rotMat is the matrix that is used to rotate the image
    # 1.0 is the scale of the image --> scale is the size of the image
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
# negative angle means anti clockwise rotation


cv.imshow('Rotated', rotated)

# flipping
flip = cv.flip(img, 0)
# 0 means flipping vertically
# 1 means flipping horizontally
# -1 means flipping both vertically and horizontally
cv.imshow('Flip', flip)

# cropping
cropped = img[0:200, 0:200]

# 200:400 means height 200 to 400 from top
cv.imshow('Cropped', cropped)


cv.waitKey(0)
# 0 is the key we have to press to close the image

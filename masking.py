import cv2 as cv
import numpy as np
img = cv.imread('Images/cat.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# masking means hiding some part of the image
circle = cv.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 100, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30),
                         (200, 200), 100, -1)

mask = cv.bitwise_and(rectangle, circle)
cv.imshow('Mask', mask)


masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)
# parameters are source image, source image, mask(optional)->mask is the image which we want to hide
cv.waitKey(0)

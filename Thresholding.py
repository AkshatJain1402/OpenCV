# thresholding is a segmentation technique used to separate an object from its background , the  image is converted to a binary image where the pixels are either 0 or 1
# we set a threshold value and if the pixel value is above the threshold value it is converted to 1 and if it is below the threshold value it is converted to 0
# thresholding is used to remove lighter or darker regions and contours are used to find the boundaries of the object

import cv2 as cv
img = cv.imread('Images/cat.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# if the pixel val is above 150 it is converted to 255 and if it is below 150 it is converted to 0
# it returns a tuple of threshold value and the thresholded image
# parameters are source image, threshold value, max value, threshold type


cv.imshow('Simple Thresholded', thresh)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)


cv.imshow('Simple Thresholded', thresh_inv)


# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# parameters are source image, max value, adaptive method, threshold type, block size(kernal size like in blur), constant that is subtracted from the mean or weighted mean calculated
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# gaussian adaptive thresholding
adaptive_thresh_gaussian = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)

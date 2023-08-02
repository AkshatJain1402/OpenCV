# contours are the boundaries of a shape with same intensity that means the contours are the boundaries of the shape with same intensity
# countours Datatype is list of numpy arrays

import numpy as np
import cv2 as cv
img = cv.imread('Images/cat.jpeg')
blank = np.zeros(img.shape, dtype='uint8')


# # convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# another way to reduce contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# if a particular pixel is smaller than 125 then it will be converted to black or 0 , or if it is above 125 it will be white or (255)
# another
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


print(len(contours))

# CHAIN_APPROX_SIMPLE returns the compressed countours points like NONE would return all the co ordinates of the line but simple would only return the end points


# RETR_LIST returns all the countours
# RETR_EXTERNAL only the external ncouontours
# RETR_TREE return all the hierarchal countours
# parameters are the image, the retrieval method and the approximation method

# countours is the list of all the contours found in the image
# hierarchies is the numpy array of the contours the hierarchy that inside a rectangle there's a square inside a sq there is a circle

# draw the contours
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('countours dranw', blank)
# parameters are the image, the contours, the index of the contours, the color of the contours and the thickness of the contours
cv.waitKey(0)

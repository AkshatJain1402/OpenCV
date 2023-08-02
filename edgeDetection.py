import cv2 as cv
import numpy as np
img = cv.imread('Images/cat.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
# parameters are source image, data type of the output image
# cv.CV_64F is the data type of the output image which decides the range of the output image
lap = np.uint8(np.absolute(lap))


cv.imshow('Laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# parameters are source image, data type of the output image, x order, y order
# x order is the order of the derivative of x
# y order is the order of the derivative of y
# if x order is 1 then it means we are calculating the first derivative of x
# if y order is 0 then it means we are calculating the zeroth derivative of y
# if x order is 2 then it means we are calculating the second derivative of x
# if y order is 1 then it means we are calculating the first derivative of y
# if x order is 0 then it means we are calculating the zeroth derivative of x
# if y order is 2 then it means we are calculating the second derivative of y
# if x order is 1 and y order is 1 then it means we are calculating the first derivative of x and first derivative of y
# if x order is 2 and y order is 2 then it means we are calculating the second derivative of x and second derivative of y

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)
cv.waitKey(0)

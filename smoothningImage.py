import cv2 as cv
import numpy as np
img = cv.imread('Images/cat.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Cat', img)

# in blur imagine a 3 row and coloumn on a specific part of image now that number of rows and cols is kernel , now we take the average of all the pixels in that kernel and replace the center pixel with that average value

# Averaging
average = cv.blur(img, (8, 8))
cv.imshow('Average Blur', average)

# guaussian blur
# difference in gaussian blur and average blur is that in gaussian blur the kernel is not a square it is a circle and the center pixel has more weightage than the other pixels in the kernel
# gaussian blur is more natural than average blur
# less blurring in gaussian blur than average blur

gauss = cv.GaussianBlur(img, (3, 3), 0)
# 0 is the standard deviation in x direction that means how much the pixels are spread in x direction
# if we increase the standard deviation the image will be more blurred

cv.imshow('Gaussian Blur', gauss)

# median blur
# in median blur we take the median of the pixels in the kernel and replace the center pixel with that median value
# median blur is used to remove the salt and pepper noise from the image
# salt and pepper noise is the white and black dots in the image
# median blur is more effective than gaussian blur in removing the salt and pepper noise
# median blur is more natural than gaussian blur
# median blur is used in medical images

median = cv.medianBlur(img, 3)
# 3 is the kernel size
cv.imshow('Median Blur', median)


# bilateral blur
# in bilateral blur we take the average of the pixels in the kernel but the pixels which are closer to the center pixel have more weightage than the pixels which are far away from the center pixel
# bilateral blur is used to preserve the edges in the image
# bilateral blur is used to remove the noise and preserve the edges
# bilateral blur is more effective than gaussian blur in removing the noise and preserving the edges
# bilateral blur is more natural than gaussian blur but less natural than median blur
# bilateral blur is used in portrait images

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)
# 10 is the diameter of the pixel neighborhood
# 35 is the sigma color value that means the color difference between the pixels and larger value for this means that more colors will be considered as neighbors, considered for blurring

# 25 is the sigma space value , larger value means that pixels farther out from the center pixel will influence the blurring calculation
cv.waitKey(0)

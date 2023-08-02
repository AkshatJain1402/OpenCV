import cv2 as cv
import numpy as np

# pixel is turned of it has a value of 0 and if it is turned on it has a value of 1
# 0 is black and 1 is white
blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)
# parameters are the two images on which we want to perform the bitwise operation
# it took the common part of the two images and made it white and the rest black

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
# it took both intersecting and non intersecting parts of the two images and made it white
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
# it took the non intersecting parts of the two images and made it white
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
# it inverted the colors of the image
# takes only one image as parameter
cv.imshow('Bitwise NOT', bitwise_not)


cv.imshow('Blank', rectangle)
cv.waitKey(0)

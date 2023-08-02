import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Cat', img)
# split the image into its color channels i.e BGR

b, g, r = cv.split(img)
# cv.imshow('Blue1', b)
# cv.imshow('Green1', g)
# cv.imshow('Red', r)

# the light color in image shows the intensity of that color in the image
# the dark color in image shows the less intensity of that color in the image

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge the color channels
merged = cv.merge([b, g, r])
# parameters are list of channels

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
# first parameter blank means black color.


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)

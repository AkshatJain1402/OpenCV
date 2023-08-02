import cv2 as cv

# in libraries like matplotlib the color spaces are RGB so where there os blue in image it is red in matplotlib and vice versa
# in opencv the color spaces are BGR so where there is blue in image it is blue in opencv

img = cv.imread('Images/cat.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cannot convert grayscale to HSV or LAB
# HSV means hue saturation value
# what is HSV? it

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

hsvToBgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsvToBgr)
# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.imshow('Cat', img)
cv.waitKey(0)

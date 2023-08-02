import numpy as np
import cv2 as cv
img = cv.imread('Images/cat.jpeg')
# cv.imshow('Cat', img)
# shape[:2] means only height and width
blank = np.zeros((500, 500, 3), dtype='uint8')

# np.zeros is a function which creates a black image where 3 is the number of channels
# channels are BGR ,BGR is blue green red , channels are the colors of the image , 3 means 3 colors

# paint the image a certain color
# blank[:] means all the pixels blank[200:300, 300:400] means only the pixels in that range


# blank[:300] = 0, 255, 0
#
# 200:300 means height 200 to 300 from top
# blank[ start: end #for height, start: end #for width]


# draw a rectangle
# list of parameters are image, start point , end point, color, thickness
# cv.rectangle(blank, (0, 0), (400, 410), (0, 255, 0), thickness=2)
# or we can use this
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=2)


# draw a circle
cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 40, (0, 0, 255), thickness=2)
# list of parameters are image, center point, radius, color, thickness
# blank.shape[1]//2 means width of the image at the end of it is the centre point
# we have to give the centre point from both height and width


# draw a line
cv.line(blank, (0, 0), (100, 100), (0, 255, 0), thickness=2)
cv.line(blank, (110, 110), (200, 200), (0, 255, 255), thickness=1)
# these start point and end point are the coordinates of the image assume a x,y axis


# write text
cv.putText(blank, 'Hello', (0, 225), cv.FONT_HERSHEY_PLAIN,
           1.0, (0, 255, 0), thickness=1)
# parameters are image, text, start point, font, scale, color, thickness

cv.imshow('Rectangle ss', blank)

# start point is top left corner
# (250,250) is bottom right corner
# where firat 250 is width and second 250 is height


cv.waitKey(0)

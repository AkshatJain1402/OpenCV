import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# masking means hiding some part of the image
circle = cv.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 100, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30),
                         (200, 200), 100, -1)

mask = cv.bitwise_and(rectangle, circle)
cv.imshow('Mask', mask)


masked_img = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked Image', masked_img)

# GRAYSCALE HISTOGRAM
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# param1: image, param2: channels, param3: mask, param4: histSize, param5: ranges
# histsize is the number of bins that is used to calculate the histogram


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# COLOR HISTOGRAM
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)

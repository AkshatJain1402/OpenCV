import cv2 as cv
import numpy as np


QR_DISTORTED = cv.imread('Images\QR_code_challenge.jpg')
blank = np.zeros(QR_DISTORTED.shape[:2], dtype='uint8')

canny1 = cv.Canny(QR_DISTORTED, 200, 355)
gray = cv.cvtColor(QR_DISTORTED, cv.COLOR_BGR2GRAY)
cv.imshow('Canny1', canny1)
canny = cv.Canny(QR_DISTORTED, 300, 350)
# inverting colors of the canny image
canny2 = cv.bitwise_not(canny)

blur = cv.GaussianBlur(canny, (3, 3), cv.BORDER_DEFAULT)


countours, hierarchies = cv.findContours(
    gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.imshow('Contours', blank)

cv.drawContours(blank, countours, -1, (255, 255, 255), 10)


# Find the contour with the maximum area
contour = max(countours, key=cv.contourArea)


# Create a mask image with the same dimensions as the input image
mask = np.zeros_like(QR_DISTORTED, dtype=np.uint8)

# Draw the contour filled with white on the mask image
cv.drawContours(mask, [contour], 0, (255, 255, 255), thickness=cv.FILLED)
cv.imshow('Mask', mask)

# Convert the mask image to grayscale
gray_mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)


# Calculate the white pixel count in the masked region
white_pixel_count = cv.countNonZero(gray_mask)
print(white_pixel_count)

# Find the bounding rectangle of the contour
x, y, w, h = cv.boundingRect(contour)

# Draw the bounding rectangle on the original image
cv.rectangle(QR_DISTORTED, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv.imshow('QR Code Region', QR_DISTORTED)


QR = cv.QRCodeDetector()

data, bbox, straight_qrcode = QR.detectAndDecode(canny)


if len(data) > 0:
    # Draw bounding box around the QR code
    for box in bbox:
        cv.polylines(canny, [box.astype(int)],
                     True, (0, 255, 0), thickness=2)

    # Extract the curved QR code region
    roi = canny[bbox[0][0][1]:bbox[0]
                       [2][1], bbox[0][0][0]:bbox[0][2][0]]
else:
    print('QR code not detected')


cv.waitKey(0)


# detect faces in a video stream

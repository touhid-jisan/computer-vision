import numpy as np
import cv2
from PIL import Image

def convert_to_hsv(img, hsv):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", imgHsv)
    # cv2.waitKey(0)

    lower = np.array([hsv[0], hsv[1], hsv[2]])
    upper = np.array([hsv[3], hsv[4], hsv[5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    # imgResult = cv2.bitwise_and(imgHsv, img, mask=mask)
    # cv2.imshow("hsv3", imgResult)
    # cv2.waitKey(0)
    return mask
# hsv = [0, 0, 165, 179, 255, 255] # for yes no
hsv_max_border = [0, 69, 103, 179, 255, 255] # for maxium bordoer 
img = cv2.imread('./images/yes.png')
mask = convert_to_hsv(img, hsv_max_border)
cv2.imshow('mask1', mask)
# Gel all pixels in the image - where BGR = (34, 33, 33), OpenCV colors order is BGR not RGB
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

gray = np.all(mask == (255, 255, 255), 2)  # gray is a logical matrix with True where BGR = (34, 33, 33).

# Convert logical matrix to uint8
gray = gray.astype(np.uint8)*255

# Find contours
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # Use index [-2] to be compatible to OpenCV 3 and 4

# Get contour with maximum area
c = max(cnts, key=cv2.contourArea)

x, y, w, h = cv2.boundingRect(c)

# Draw green rectangle for testing
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)
print(x, y, w, h)
imgresult = img[y:y+h, x:x+w]
# Show result
cv2.imshow('mask2', mask)
cv2.imshow('gray', gray)
cv2.imshow('img', img)
cv2.imshow('imgresult', imgresult)
cv2.waitKey(0)
cv2.destroyAllWindows()
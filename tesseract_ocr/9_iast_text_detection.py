import numpy as np
import cv2
import pytesseract

def convert_to_hsv(img, hsv):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsv[0], hsv[1], hsv[2]])
    upper = np.array([hsv[3], hsv[4], hsv[5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    return mask

hsv = [0, 0, 181, 179, 255, 255] # pop up text
img = cv2.imread('./images/yes.png') 
mask = convert_to_hsv(img, hsv)

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
# Gel all pixels in the image - where BGR = (34, 33, 33), OpenCV colors order is BGR not RGB
gray = np.all(mask == (255, 255, 255), 2)  # gray is a logical matrix with True where BGR = (34, 33, 33).
# Convert logical matrix to uint8
gray = gray.astype(np.uint8)*255
# Find contours
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # Use index [-2] to be compatible to OpenCV 3 and 4
# Get contour with maximum area
c = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
# Draw green rectangle for testing
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 1)
imgresult = img[y+5:y+h, x:x+w]
resized_img = cv2.resize(imgresult, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
mask = convert_to_hsv(resized_img, [0, 0, 61, 179, 255, 255])
invert = cv2.bitwise_not(mask)
img_text2 = pytesseract.image_to_string(invert, config=r'--oem 3 --psm 6')
print(img_text2)

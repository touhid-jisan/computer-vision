"""
*
* @created 2021-10-30
* @project tesseract_ocr
* @author touhidul
*
"""

import cv2
import pytesseract
import numpy as np

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\touhidul\\scoop\\apps\\tesseract\\5.0.0-alpha.20210811\\tesseract.exe'


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


img = cv2.imread('./images/full_screen.png')
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# img = img[299:366, 342:568]
# cv2.imshow('img', img)
# cv2.waitKey(0)

hsv = [0, 0, 0, 179, 255, 180]
mask = convert_to_hsv(img, hsv)

thr = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, 25, 28)
bnt = cv2.bitwise_not(thr)
txt = pytesseract.image_to_string(bnt, config="--psm 6")
print(txt)



# cv2.imshow('mask', mask)
# cv2.waitKey(0)

# invert = cv2.bitwise_not(mask)
# cv2.imshow('invert', invert)
# cv2.waitKey(0)

# gray = cv2.cvtColor(invert,cv2.COLOR_BGR2GRAY)
# _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# x,y,w,h = cv2.boundingRect(cnt)
# crop = img[y:y+h,x:x+w]
# cv2.imshow('sofwinres',crop)
# cv2.waitKey(0)



# gry = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
# # invert = cv2.bitwise_not(img)
# cv2.imshow('img', mask)
# cv2.waitKey(0)
# # invert = cv2.bitwise_not(mask)
# invert = np.invert(mask)
# cv2.imshow('img', invert)
# cv2.waitKey(0)
# data = pytesseract.image_to_string(invert, lang='eng', config='--oem 3 --psm 6')

# print(data)




# import cv2
# import numpy as np
# img = cv2.imread('./images/yes_1.png')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
# cv2.imshow('img', thresh)
# cv2.waitKey(0)

# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# x,y,w,h = cv2.boundingRect(cnt)
# crop = img[y:y+h,x:x+w]

# cv2.imshow('img', crop)
# cv2.waitKey(0)
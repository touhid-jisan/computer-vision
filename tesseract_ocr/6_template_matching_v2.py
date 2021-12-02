"""
*
* @created 2021-10-31
* @project tesseract_ocr
* @author touhidul
*
"""

import numpy as np
import cv2
import pytesseract


def confirm_menu(img, template):
    h, w = template.shape
    method = cv2.TM_CCOEFF
    #
    # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
    #             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    xx = img2[location[1]:(location[1] + h), location[0]:(location[0] + w)]
    return xx


def image_to_text(img):
    text = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 6')
    print(text)
    return text

def detectColor(img, hsv):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsv[0], hsv[1], hsv[2]])
    upper = np.array([hsv[3], hsv[4], hsv[5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    return mask

menu_image = './images/press_f2.png'
menu_template = './images/f2_message.PNG'
img = cv2.imread(menu_image, 0)
template = cv2.imread(menu_template, 0)
new_image = confirm_menu(img, template)
new_image_text = image_to_text(new_image)
cv2.imshow('xx', new_image) 
cv2.waitKey(0)
print(new_image_text)

# hsv = [26, 0, 0, 179, 255, 255]
# imgResult = detectColor(new_image, hsv)

# new_text = image_to_text(imgResult)
# print('aa ', new_text)

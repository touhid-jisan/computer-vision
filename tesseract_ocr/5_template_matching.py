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
    method = cv2.TM_CCOEFF_NORMED
    #
    # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
    #             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = max_loc
    
    threshold = 0.9
    flag = False
    if np.amax(result) > threshold:
        print(True)
        print(np.amax(result))
    # if max_val>= 0.8:
    #     print('Found {}'.format(max_val))
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    xx = img2[location[1]:(location[1] + h), location[0]:(location[0] + w)]
    # print(result)
    return xx


def image_to_text(img):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    # print(text)
    return text
def findActiveOption():
    pass

def detectColor(img, hsv):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", imgHsv)
    cv2.waitKey(0)

    lower = np.array([hsv[0], hsv[1], hsv[2]])
    upper = np.array([hsv[3], hsv[4], hsv[5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    # imgResult = cv2.bitwise_and(imgHsv, img, mask=mask)
    # cv2.imshow("hsv3", imgResult)
    # cv2.waitKey(0)
    return mask

menu_images = ['./images/full_screen.png']
menu_templates = ['./images/main.png']
for menu_image in menu_images:
    for menu_template in menu_templates:
        img = cv2.imread(menu_image, 0)
        template = cv2.imread(menu_template, 0)
        new_image = confirm_menu(img, template)
        cv2.imshow('xx', new_image)
        cv2.waitKey(0)
        text = image_to_text(new_image)
        if text.lower().find('hain') != -1:
            print('I am in Main')
            break
        elif text.lower().find('main') != -1:
            print('I am in Advanced')
            break
        elif text.lower().find('advanced') != -1:
            print('I am in Advanced')
            break
        elif text.lower().find('power') != -1:
            print('I am in Power')
            break
        elif text.lower().find('security') != -1:
            print('I am in Security')
            break
    # img = cv2.imread(menu_image)
    # cut_img = img[130:660, 100:950]
    # # cv2.imshow("hsv2", img)
    # # cv2.waitKey(0)


    # hsv = [0, 0, 0, 179, 255, 170]
    # imgResult = detectColor(img, hsv)

    # cv2.imshow("hsv2", imgResult)
    # cv2.waitKey(0)
    # new_text = image_to_text(imgResult)
    # print(new_text)


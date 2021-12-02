from re import T
from typing import Text
import numpy as np
import cv2
import pytesseract
import pyautogui

# from windowcap import WindowCap

class PopupText:

    def __init__(self, text):
        self.hsv = [0, 0, 181, 179, 255, 255]
        self.text = text
    
    def convert_to_hsv(self, img, hsv):
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([hsv[0], hsv[1], hsv[2]])
        upper = np.array([hsv[3], hsv[4], hsv[5]])
        mask = cv2.inRange(imgHsv, lower, upper)
        return mask
        
    def get_popup_text(self):
        while(True):
            # wincap = WindowCap()
            # img = wincap.get_screenshot()
            img = cv2.imread('./images/no.png')
            mask = self.convert_to_hsv(img, self.hsv)

            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
            gray = np.all(mask == (255, 255, 255), 2) 
            gray = gray.astype(np.uint8)*255
            cv2.imshow('gray', gray)
            cv2.waitKey(0)
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
            c = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            imgresult = img[y+5:y+h, x:x+w]
            mask = self.convert_to_hsv(imgresult, [0, 0, 61, 179, 255, 255])
            invert = cv2.bitwise_not(mask)
            cv2.imshow('invert', invert)
            cv2.waitKey(0)
            converted_text = pytesseract.image_to_string(invert, config=r'--oem 3 --psm 6', lang='eng')
            print(converted_text)
            if converted_text.find(self.text) != -1:
                return True
            else:
                pyautogui.press('down')
    


popup = PopupText('No')
text_flag = popup.get_popup_text()
print(text_flag)
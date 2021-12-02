from re import T
import time
from typing import Text
import numpy as np
import cv2
import pytesseract
import pyautogui

# not finished
class PopupText:

    def __init__(self, possible_text, press_text):
        self.hsv = [0, 80, 128, 179, 245, 255]
        self.possible_text = possible_text
        self.press_text = press_text
    
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
            img = cv2.imread('./images/yes.png')
            img_copy = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
            mask = self.convert_to_hsv(img_copy, self.hsv)
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
            gray = np.all(mask == (255, 255, 255), 2) 
            gray = gray.astype(np.uint8)*255
            cv2.imshow('invert', gray)
            cv2.waitKey(0)
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
            
            c = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('drawContour', img_copy)
            cv2.waitKey(0)
            print(x, y, w, h)
            imgresult = img_copy[y:y+h, x:x+w]
            # resized_img = cv2.resize(imgresult, None, fx=2.3, fy=2.3, interpolation=cv2.INTER_CUBIC)
            mask = self.convert_to_hsv(imgresult, [0, 0, 92, 179, 255, 255])
            blur = cv2.blur(mask,(2,2))
            invert = cv2.bitwise_not(blur)
            cv2.imshow('invert', invert)
            cv2.waitKey(0)
            # removing black bg from yes/no
            mask = cv2.cvtColor(invert, cv2.COLOR_BGR2RGB)
            gray = np.all(mask == (255, 255, 255), 2) 
            gray = gray.astype(np.uint8)*255
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
            c = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            print(x, y, w, h)
            imgresult = invert[y:y+h, x:x+w]

            cv2.imshow('imgresult', imgresult)
            cv2.waitKey(0)
            converted_text = pytesseract.image_to_string(imgresult, config='--oem 3 --psm 6', lang='eng')
            for element in self.possible_text:
                if converted_text.find(element) != -1:
                    print(element)
                    return True
            
            pyautogui.press(self.press_text)
            time.sleep(1)
    

popup = PopupText(['English'], 'down')
text_flag = popup.get_popup_text()
print(text_flag)
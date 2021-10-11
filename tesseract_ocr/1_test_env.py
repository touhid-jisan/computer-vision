"""
*
* @created 2021-10-10
* @project pyautogui
* @author touhidul
*
"""

import pytesseract
import cv2
from PIL import Image # pillow library
import pkg_resources

# declaring the exe path for tesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\touhidul\\scoop\\apps\\tesseract\\5.0.0-alpha.20210811\\tesseract.exe'

print(pkg_resources.working_set.by_key['pytesseract'].version)
print(cv2.__version__)
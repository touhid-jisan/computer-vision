"""
*
* @created 2021-11-04
* @project tesseract_ocr
* @author touhidul
*
"""
import numpy as np
import cv2

main_img = cv2.imread('/images/main.png', 0)
temp_img = cv2.imread('./images/cropped/main.png', 0)

h, w = temp_img.shape

result = cv2.matchTemplate(main_img, temp_img, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
location = max_loc
bottom_right = (location[0] + w, location[1] + h)
cv2.rectangle(main_img, location, bottom_right, 255, 5)
cv2.imshow('Match', main_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

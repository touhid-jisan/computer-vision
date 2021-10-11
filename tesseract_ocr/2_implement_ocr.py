"""
*
* @created 2021-10-10
* @project computer-vision
* @author touhidul
*
"""
import pytesseract
import pkg_resources
import cv2
import re
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\touhidul\\scoop\\apps\\tesseract\\5.0.0-alpha.20210811\\tesseract.exe'

# loading the image from the disk
image_to_ocr = cv2.imread('images/testing/fox.jpg')

# preprocessing the image
# step 1: convert to grey scale
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
# step 2: do binary and otsu thresholding
preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# step 3: Smooth the image using median blur
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

# save the preprocessed image temporarily into the disk
cv2.imwrite('images/testing/temp_fox.jpg', preprocessed_img)
# load the temporary image as a PIL/Pillow image
preprocessed_pil_img = Image.open('images/testing/temp_fox.jpg')

# pass the pil image to tesseract to do ocr
text_extracted = pytesseract.image_to_string(preprocessed_pil_img)

# print the text
print(text_extracted)
text_extracted = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text_extracted)
print(text_extracted)

cv2.imshow("Actual Image", image_to_ocr)
cv2.waitKey(0)


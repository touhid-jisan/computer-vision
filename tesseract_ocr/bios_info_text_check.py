import cv2
import numpy as np
import pytesseract
from pytesseract.pytesseract import Output

img = cv2.imread('./syste_info.png')
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower = np.array([0, 0, 145])
upper = np.array([179, 255, 255])
mask = cv2.inRange(imgHsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('threshold image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

custom_config = r'--oem 3 --psm 6'
# now feeding image to tesseract
details = pytesseract.image_to_data(mask, output_type=Output.DICT, config=custom_config, lang='eng')

parse_text = []
word_list = []
last_word = ''
for word in details['text']:
    if word!='':
        word_list.append(word)
        last_word = word
    if (last_word!='' and word == '') or (word==details['text'][-1]):
        parse_text.append(word_list)
        word_list = []
import csv
with open('result_tsext.txt',  'w', newline="") as file:
    csv.writer(file, delimiter=" ").writerows(parse_text)
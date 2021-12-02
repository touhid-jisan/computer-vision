import cv2
import numpy as np
import pytesseract
def autocrop(image, threshold=0):
    if len(image.shape) == 3:
        flatImage = np.max(image, 2)
    else:
        flatImage = image
    assert len(flatImage.shape) == 2

    rows = np.where(np.max(flatImage, 0) > threshold)[0]
    if rows.size:
        cols = np.where(np.max(flatImage, 1) > threshold)[0]
        image = image[cols[0]: cols[-1] + 1, rows[0]: rows[-1] + 1]
    else:
        image = image[:1, :1]

    return image

def convert_to_hsv(img, hsv):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsv[0], hsv[1], hsv[2]])
    upper = np.array([hsv[3], hsv[4], hsv[5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    return mask


img = cv2.imread('./images/english.png')
img = img[299:366, 342:568]
# img = img[299:366, 300:600]
cv2.imshow("hsv3", img)
cv2.waitKey(0)
hsv = [0, 0, 20, 179, 255, 255]
mask = convert_to_hsv(img, hsv)
invert = cv2.bitwise_not(mask)
img = autocrop(invert)
data = pytesseract.image_to_data(img, lang='eng', config='--oem 3 --psm 7')
print(data)

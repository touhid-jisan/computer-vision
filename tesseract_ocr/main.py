import cv2
import os
from time import time
import pytesseract
import numpy as np
from windowcapture import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WindowCapture.list_window_name()

wincap = WindowCapture('File Explorer')
loop_time = time()
while(True):
    screenshoot = wincap.get_screenshot()
    img = cv2.imread('./bios/images/main.png', 0)
    template = cv2.imread('./bios/images/menubar.PNG', 0)

    # print(np.shape(screenshoot))
    # screenshoot = np.array(screenshoot)
    screenshoot = cv2.cvtColor(screenshoot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshoot, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    flag = False
    print(np.amax(result))
    if np.amax(result) > threshold:
        print(True)
        print(np.amax(result))
        break







    # screenshoot = np.array(screenshoot)
    # screenshoot = cv2.cvtColor(screenshoot, cv2.COLOR_RGB2BGR)
    
#     cv2.imshow('Computer Vision', screenshoot)
#     data = pytesseract.image_to_string(screenshoot, lang='eng', config='--oem 3')
#     string = 'Press <F2> to enter Setup or <F12> to enter Boot Menu.'
#     if string in data:
#         print(data)
#         print(True)
#         cv2.destroyAllWindows()
#         break 
 
#     print('FPS : {}'.format(1/ (time() - loop_time)))
#     loop_time = time()  
#     if cv2.waitKey(1) == ord('q'):
#         cv2.destroyAllWindows()
#         break 

# print('[INFO] Done')
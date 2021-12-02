import cv2
import numpy as np
import os
from PIL import ImageGrab
from time import time
import win32gui, win32ui, win32con
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def list_window_name():
    def windEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(windEnumHandler, None)

list_window_name()
# def window_capture():
#     w = 1920 # set this
#     h = 1080 # set this
#     # bmpfilenamename = "out.bmp" #set thisq

#     hwnd = win32gui.FindWindow(None, 'Fast Window Capture - OpenCV Object Detection in Games #4 - YouTube - Google Chrome')

#     # get the window image data 
#     wDC = win32gui.GetWindowDC(hwnd)
#     dcObj=win32ui.CreateDCFromHandle(wDC)
#     cDC=dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

#     # save the screenshot
#     # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
#     # instead of saving we will return it

#     signedIntsArray = dataBitMap.GetBitmapBits(True)
#     img = np.fromstring(signedIntsArray, dtype='uint8')
#     img.shape = (h, w, 4)

#     # Free Resources
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(hwnd, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())

#     return img


# loop_time = time()
# while(True):
#     screenshoot = window_capture()
#     # screenshoot = np.array(screenshoot)
#     # screenshoot = cv2.cvtColor(screenshoot, cv2.COLOR_RGB2BGR)

#     cv2.imshow('Computer Vision', screenshoot)
 
#     print('FPS : {}'.format(1/ (time() - loop_time)))
#     loop_time = time()
#     if cv2.waitKey(1) == ord('q'):
#         cv2.destroyAllWindows()
#         break 

# print('[INFO] Done')
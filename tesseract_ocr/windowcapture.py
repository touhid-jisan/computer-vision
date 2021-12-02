
import numpy as np
import win32gui, win32ui, win32con
import cv2
from PIL import Image
class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0

    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()

        else:
            # self.hwnd = win32gui.FindWindow(None, window_name)
            # if not self.hwnd:
            #     self.hwnd = win32gui.GetDesktopWindow()
            self.hwnd = win32gui.FindWindow(None, 'getit | oVice - Google Chrome')
            win32gui.SetForegroundWindow(self.hwnd)
        # get the window size
        left, top, right, bot  = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2]-window_rect[0]
        self.h = window_rect[3]-window_rect[1]

        # acount for the window border and tiitle bar to cut out
        border_pixels = 8
        titlebar_pixels = 30

        self.w = self.w - (2*border_pixels)
        self.h = self.h - titlebar_pixels - border_pixels

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

    def get_screenshot(self):
        # bmpfilenamename = "out.bmp" #set thisq

        
        # get the window image data 
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0, 0), win32con.SRCCOPY)

        # save the screenshot
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        # instead of saving we will return it

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        ###############
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        img = Image.frombuffer('RGB',(bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
        ##########

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)
        return img
    @staticmethod
    def list_window_name():
        def windEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(windEnumHandler, None)
    
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x + pos[1] + self.offset_y)



wincap = WindowCapture('getit | oVice - Google Chrome')
scr = wincap.get_screenshot()
screenshot = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
cv2.imshow('as', screenshot)
cv2.waitKey(0)

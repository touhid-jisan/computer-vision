
import numpy as np
import win32gui, win32ui, win32con
from PIL import Image 
import cv2
import time
class WindowCapture:

    w = 0
    h = 0
    left = 0
    top = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0

    offset_x = 0
    offset_y = 0

    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2]-window_rect[0]
        self.h = window_rect[3]-window_rect[1]
        self.left = window_rect[0]
        self.top = window_rect[1]
        win32gui.SetForegroundWindow(self.hwnd)
        # acount for the window border and tiitle bar to cut out
        border_pixels = 8
        titlebar_pixels = 30

        self.w = self.w - (2*border_pixels)
        self.h = self.h - titlebar_pixels - border_pixels

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

    def get_screenshot(self):
        hdesktop = win32gui.GetDesktopWindow()
        wDC = win32gui.GetWindowDC(hdesktop)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.left, self.top), win32con.SRCCOPY)

        # for black screen problem
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        img = Image.frombuffer('RGB',(bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
        #
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        # convert PIL image to CV2
        open_cv_image = np.array(img) 
        # Convert RGB to BGR 
        img = open_cv_image[:, :, ::-1].copy()
        return img
    @staticmethod
    def list_window_name():
        def windEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(windEnumHandler, None)
    
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x + pos[1] + self.offset_y)

try:
    WindowCapture.list_window_name()
    wincap = WindowCapture('Facebook - Google Chrome')
    scr = wincap.get_screenshot()
    # print(type(scr))
    # cv2.imshow('sda', scr)
    # cv2.waitKey(0)
except Exception as e:
    print('[ERROR] : {}'.format(e))
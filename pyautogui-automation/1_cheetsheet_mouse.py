"""
*
* @created 2021-10-11
* @project computer-vision
* @author touhidul
*
"""
import pyautogui

# General Functions
print(pyautogui.position())  # current mouse x and y
print(pyautogui.size())  # c    urrent screen resolution width and height
print(pyautogui.onScreen(300, 300))

# Fail-Safes
pyautogui.PAUSE = 2.5  # Set up a 2.5 second pause after each PyAutoGUI call
pyautogui.FAILSAFE = True  # When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program

# Mouse Functions
pyautogui.moveTo(10, 10, duration=1)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(10, 10, duration=1)  # move mouse relative to its current position

pyautogui.moveTo(100, 100)  # If duration is 0 or unspecified
pyautogui.moveRel(100, 200)  # If duration is 0 or unspecified

pyautogui.dragTo(600, 310)  # drag mouse to XY
pyautogui.dragRel(600, 310)

# Mouse Functions - example 1
distance = 50
x= 0
for i in range(4):
    pyautogui.moveTo(500+x, 500)
    pyautogui.dragRel(0, distance)
    pyautogui.dragRel(distance, 0)
    pyautogui.dragRel(0, -distance)
    pyautogui.dragRel(-distance, 0)
    x += 200

pyautogui.click(712, 443, 2, button='right')  # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

pyautogui.rightClick(900, 500)
pyautogui.leftClick(500, 900)
pyautogui.doubleClick(900, 500)
pyautogui.tripleClick(900, 500)


pyautogui.scroll(1000000, 900, 1)  #
pyautogui.scroll(10)   # scroll up 10 "clicks"
pyautogui.scroll(-10)  # scroll down 10 "clicks"
pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

pyautogui.hscroll(10)   # scroll right 10 "clicks"
pyautogui.hscroll(-10)  # scroll left 10 "clicks"

pyautogui.vscroll(-4)
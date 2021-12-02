
import pyautogui
x = pyautogui.confirm(text='Message: Error Occurred\nDo you want to start from beginning? \n\nメッセージ：エラーが発生しました\n最初から始めたいですか？', title='Notification', buttons=['Yes', 'Cancel'])
print(x)
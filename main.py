import pyautogui
import time

image = 'test.png'

time.sleep(2)
while True:
    go = pyautogui.locateOnScreen(image, confidence=0.9)
    print (go)
    pyautogui.click(go)
    
# press ctrl + c to exit/stop

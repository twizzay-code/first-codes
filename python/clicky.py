#! python3
import pyautogui
from time import sleep

repeat = int(input("How many times would you like to clickify? :"))
startpos = pyautogui.position()
count = 1

#opens the correct screen if command is being executed on another screen.
pyautogui.click()

while count <= repeat:

    sleep(75)
    pyautogui.click()
    pyautogui.moveTo(x=865, y=326)
    sleep(1)
    pyautogui.click()
    sleep(3)
    pyautogui.moveTo(x=539, y=565)
    pyautogui.click()
    sleep(5)
    pyautogui.moveTo(x=1757, y=1045)
    pyautogui.click(clicks=2, interval=5)
    pyautogui.moveTo(x=848, y=306)
    pyautogui.click()
    sleep(3)
    pyautogui.moveTo(x=765, y=325)
    pyautogui.click()
    sleep(3)
    pyautogui.moveTo(x=822, y=309)
    pyautogui.click()
    sleep(5)
    pyautogui.moveTo(x=96, y=67)
    pyautogui.click()
    pyautogui.moveTo(startpos)

    count = count + 1

exit()

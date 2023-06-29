from pyautogui import *
import pyautogui
import time
import datetime
import keyboard
import random
import win32api, win32con
import sys
i = 0
while(i<30):
    x , y = pyautogui.position()
    print(f'{x},{y}')
    i = i + 1
    time.sleep(0.5)

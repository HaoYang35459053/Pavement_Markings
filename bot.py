from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Tile 1 Position X: 778, Y: 933
# Tile 2 Position X: 885, Y: 933
# Tile 3 Position X: 1012, Y: 933
# Tile 4 Position X: 1115, Y: 933

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(778, 933)[0] == 0:
        click(778, 933)
    if pyautogui.pixel(885, 933)[0] == 0:
        click(885, 933)
    if pyautogui.pixel(1012, 933)[0] == 0:
        click(1012, 933)
    if pyautogui.pixel(1115, 933)[0] == 0:
        click(1115, 933)

# The function of the program:
# This program will play the piano tile game itself

# This is the work copied and derived from the video on YouTube:
# How to make advanced image recognition bots using python made by Kian Brose
# https://www.youtube.com/watch?v=YRAIUA-Oc1Y&t=221s

# The game: https://www.agame.com/game/magic-piano-tiles
# The tile positions are collected by the Program: Mouse_Positions_1.py

from pyautogui import *
import pyautogui  # Import the pyautogui library for mouse and keyboard control
import time  # Import the time library for sleep function
import keyboard  # Import the keyboard library for keyboard control
import win32api, win32con  # Import win32api and win32con for Windows API functions

# Tile positions
# Tile 1 Position X: 410, Y: 480
# Tile 2 Position X: 552, Y: 480
# Tile 3 Position X: 642, Y: 480
# Tile 4 Position X: 779, Y: 480

def click(x, y):
    win32api.SetCursorPos((x, y))  # Move the cursor to the specified position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)   # Simulate mouse left button down
    time.sleep(0.05)                                            # Small delay to simulate the click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)     # Simulate mouse left button up


while keyboard.is_pressed('q') == False:  # Loop until 'q' is pressed
    
    if pyautogui.pixel(410, 480)[0] == 0:   # Check if the pixel at (410, 480) is black (R value is 0)
        click(410, 480)                     # Click at the position (410, 480)
    if pyautogui.pixel(552, 480)[0] == 0:   # Check if the pixel at (552, 480) is black
        click(552, 480)                     # Click at the position (552, 480)
    if pyautogui.pixel(642, 480)[0] == 0:   # Check if the pixel at (642, 480) is black
        click(642, 480)                     # Click at the position (642, 480)
    if pyautogui.pixel(779, 480)[0] == 0:   # Check if the pixel at (779, 480) is black
        click(779, 480)                     # Click at the position (779, 480)
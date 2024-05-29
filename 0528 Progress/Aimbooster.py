# The function of the program:
# The program plays the aimbooster game
# The game link:
# http://www.aimbooster.com/

# The codes of the program is basically copied from the video made by Kian Brose
# The video link:
# https://www.youtube.com/watch?v=YRAIUA-Oc1Y&t=603s

from pyautogui import *     # Import all functions from pyautogui
import pyautogui            # Import pyautogui library for GUI automation
import time                 # Import time library for sleep function
import keyboard             # Import keyboard library to detect key presses
import random               # Import random library for random number generation
import win32api, win32con   # Import win32api and win32con for Windows API functions

time.sleep(2)               # Wait for 2 seconds before starting the script

def click(x, y):
    win32api.SetCursorPos((x, y))                               # Move the cursor to the specified (x, y) position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)   # Simulate mouse left button down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)     # Simulate mouse left button up

# Color of center: (255, 219, 195)
while keyboard.is_pressed('q') == False:                    # Loop until 'q' is pressed
    pic = pyautogui.screenshot(region=(82, 439, 770, 540))  # Take a screenshot of the specified region
    width, height = pic.size                                # Get the width and height of the screenshot

    for x in range(0, width, 5):            # Iterate over the width of the screenshot in steps of 5 pixels
        for y in range(0, height, 5):       # Iterate over the height of the screenshot in steps of 5 pixels
            r, g, b = pic.getpixel((x, y))  # Get the RGB values of the pixel at (x, y)
            if b == 195:                    # Check if the blue component of the pixel is 195
                click(x + 82, y + 439)      # Click at the adjusted position (accounting for the screenshot region offset)
                time.sleep(0.05)            # Wait for 0.05 seconds before the next action
                break                       # Exit the inner loop once a click is performed

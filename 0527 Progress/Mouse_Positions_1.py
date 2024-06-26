# The function of the program:
# The program keeps printing the position of the mouse on the screen.

# The codes is basically copied from the video made by Parwiz Forogh on YouTube: 
# Video name: Python Automating GUI Getting Mouse Position | PyAutoGUI Tutorials
# The video link:
# https://www.youtube.com/watch?v=tnbMdtcUQew

# Version 1 (There is another version of the program)
import pyautogui  # Import the pyautogui library for mouse and keyboard control
import time

# Uncomment the following line to print the current mouse position once
# print(pyautogui.position())

try:
    while True:  # Start an infinite loop
        x, y = pyautogui.position() # Get the current mouse cursor position
        # Format the position as a string with X and Y coordinates right-justified to width 4
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)  # Print the formatted position string
        time.sleep(0.5)  # Pause for 0.5 seconds before recording the next position

except KeyboardInterrupt:   # Handle the keyboard interrupt (Ctrl+C)
    print('\nDone.')        # Print a message and exit the loop gracefully
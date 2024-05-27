# Version 1
import pyautogui  # Import the pyautogui library for mouse and keyboard control

# Uncomment the following line to print the current mouse position once
# print(pyautogui.position())

try:
    while True:  # Start an infinite loop
        x, y = pyautogui.position() # Get the current mouse cursor position
        # Format the position as a string with X and Y coordinates right-justified to width 4
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr)  # Print the formatted position string

except KeyboardInterrupt:   # Handle the keyboard interrupt (Ctrl+C)
    print('\nDone.')        # Print a message and exit the loop gracefully
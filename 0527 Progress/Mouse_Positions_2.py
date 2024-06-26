# The function of the program:
# The program keeps printing the position of the mouse on the screen.

# The codes is derived from the video made by Parwiz Forogh on YouTube: 
# Video name: Python Automating GUI Getting Mouse Position | PyAutoGUI Tutorials
# The video link:
# https://www.youtube.com/watch?v=tnbMdtcUQew

# Version 2 (There is Version One)
import pyautogui    # Import the pyautogui library for mouse and keyboard control
import threading    # Import the threading library for multi-threading support

stop_thread = False # Global variable to control the stopping of the thread

def monitor_position():
    try:
        while not stop_thread:  # Loop until stop_thread is set to True
            x, y = pyautogui.position()  # Get the current mouse cursor position
            # Format the position as a string with X and Y coordinates right-justified to width 4
            positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
            print(positionStr)  # Print the formatted position string
            time.sleep(0.5)  # Pause for 0.5 seconds before recording the next position
    except Exception as e:  # Catch any exceptions that occur
        print(f"An error occurred: {e}")  # Print the error message
    finally:
        print('Done.')  # Print a message when the loop is done

def stop_program():
    global stop_thread  # Declare stop_thread as a global variable
    input("Press Enter to stop the program...")  # Wait for user input to stop the program
    stop_thread = True  # Set stop_thread to True to stop the monitoring loop

# Start the position monitoring in a separate thread
thread = threading.Thread(target=monitor_position)
thread.start()  # Start the thread

# Start the stop_program function to wait for user input
stop_program()

# Wait for the thread to finish
thread.join()  # Ensure the main program waits for the thread to complete
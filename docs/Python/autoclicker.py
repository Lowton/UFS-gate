#################################################
## Name of Program: AutoClicker
## Description:		It simply auto clicks nuff said :P 
## Authour(s):		Al Bedouin (Render)
#################################################

# Import anything we need
import win32api, win32con, time, os

# Create a function that simply prints a new line.
def NewLine():
	print("")

# Simply check if the variables are numbers.
def CheckIfNumber(number):
	try: # Try to see if the character(s) that were inputted were numbers.
   		 value = float(number) # Check if the the value is a float, which allows decimals, unlike int.

   		 return value # If All went well, return the value.
	except ValueError: # If the character was NOT an integer throw an error.
   		input("Error: Invalid Input! Input must be a number! ")
   		quit()

# Define the number of clicks we want to do
print("[AutoClicker] Welcome to Render's AutoClicker v1.0")

# Print up start up shit blah blah blah...

# The amount of clicks
NumberofClicks = input("[AutoClicker] Input the number of times you to click: ")
CheckIfNumber(NumberofClicks)

# The time in between each click. (In Seconds)
Delay = input("[AutoClicker] How often do you want to click. (In Seconds): ")
CheckIfNumber(Delay)
NewLine()

# This will simply use the left button of the mouse without user interaction.
def click(amount):
    i = 1
    while (i <= int(amount)):
	    print("[AutoClicker] Clicked [" + str(i) + "] amount of times.")
	    i = i + 1	
	    x, y = win32api.GetCursorPos()
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	    time.sleep(int(Delay))

# Record how long it took to conduct the clicks.
timer1 = time.time()
click(NumberofClicks)
timer2 = time.time()
total = timer2 - timer1

# Print the amount of clicks done and how long it took.
print("[AutoClicker] Finished! Clicked " + str(NumberofClicks) + " times in " + str(round(total, 2)) + "s")
os.system("pause")

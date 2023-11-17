import time
import pyautogui
import datetime

# This disables the script terminating when  the mouse pointer moves to any corners of the screen 
pyautogui.FAILSAFE=False

# Defining now attribute to get the current datof the system and use it for the specific interval
now = datetime.datetime.now()
# print (now .year,  now . month,  now. day,  now. hour,  now. minute, now. second)
# 2015 5 6 8 53 40
print("Current time is", now.strftime("%H:%M"))

# Function to move the cursor for every 1 second
def executeSomething():
    pyautogui.moveTo(200, 200, duration = 1)
    pyautogui.moveRel(200, 25, duration = 1)

# method to click the shift button for every loop
    pyautogui.press('shift')
    time.sleep(290)

# Loop - continues till the above  function is true. 
while  True:
    now = datetime.datetime.now()
#if 6 < now.hour and 19 >  now.hour:
    if 6 < now.hour  and  17  >  now.hour:
        executeSomething()
    else:
        print("Detected out of office-hours, exiting now...")
        exit()
import webbrowser
import time
import os
from datetime import datetime


'''
Utility functions
'''
def continueDay():
    cont = input("Press ENTER too continue")

'''
Start here
'''
os.system("bash logSystemOnOff.sh") 

# sendNotificationOnWindows("How was the workout? Share with Penzu")
print("How was the workout? Share with Penzu")
webbrowser.open(os.getenv(PENZU))
continueDay()

# notion
print("Check your calendar")
print("Update Daily Tasks")
webbrowser.open_new_tab(os.getenv(NOTION))
continueDay()

# start touch type measure and practice
print("test 1")
webbrowser.open(os.getenv(TEST1))
continueDay()
print("test 2")
webbrowser.open(os.getenv(TEST2))
continueDay()
print("test 3")
webbrowser.open(os.getenv(TEST3))
continueDay()
print("test 4")
webbrowser.open(os.getenv(TEST4))
continueDay()

# cal & update daily type progess
print("WPM daily update")
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
webbrowser.open(os.getenv(T_WORKSHEET))
continueDay()

# anki
print("Anki time!")
webbrowser.open(os.getenv(ANKI))
continueDay()

# mail
print("Check mail")
webbrowser.open(os.getenv(MAIL))
continueDay()

# whatsapp
print("Check whatsapp")
# sendNotificationOnWindows("Open Whatsapp")
webbrowser.open(os.getenv(WHATSAPP))
continueDay()

# leetcode
print("DSA Practice")
webbrowser.open(os.getenv(LEETCODE))
continueDay()

print("Let's take a bread!")
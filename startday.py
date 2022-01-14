import webbrowser
import time
import os
from datetime import datetime
from dotenv import load_dotenv

flag = load_dotenv()

if not flag:
    alt = "https://www.google.com/"

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
webbrowser.open(os.getenv("PENZU",alt))
continueDay()

# notion
print("Check your calendar")
print("Update Daily Tasks")
webbrowser.open_new_tab(os.getenv("NOTION",alt))
continueDay()

# start touch type measure and practice
print("test 1")
webbrowser.open(os.getenv("TEST1",alt))
continueDay()
print("test 2")
webbrowser.open(os.getenv("TEST2",alt))
continueDay()
print("test 3")
webbrowser.open(os.getenv("TEST3",alt))
continueDay()
print("test 4")
webbrowser.open(os.getenv("TEST4",alt))
continueDay()

# cal & update daily type progess
print("WPM daily update")
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
webbrowser.open(os.getenv("T_WORKSHEET",alt))
continueDay()

# anki
print("Anki time!")
webbrowser.open(os.getenv("ANKI"),alt)
continueDay()

# mail
print("Check mail")
webbrowser.open(os.getenv("MAIL",alt))
continueDay()

# whatsapp
print("Check whatsapp")
# sendNotificationOnWindows("Open Whatsapp")
webbrowser.open(os.getenv("WHATSAPP",alt))
continueDay()

# leetcode
print("DSA Practice")
webbrowser.open(os.getenv("LEETCODE",alt))
continueDay()

print("Let's take a bread!")
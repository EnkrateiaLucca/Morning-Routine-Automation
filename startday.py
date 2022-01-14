import webbrowser
import time
import os
from datetime import datetime
from dotenv import load_dotenv

flag = load_dotenv()

alt = ""
if not flag:
    alt = "https://www.google.com/"

'''
Utility functions
'''
def continueDay():
    cont = input("Press ENTER too continue")

def printMessage(message=""):
    print(message)
    time.sleep(1)

'''
Start here
'''
os.system("bash logSystemOnOff.sh") 

# sendNotificationOnWindows("How was the workout? Share with Penzu")
printMessage("How was the workout? Share with Penzu")
webbrowser.open(os.getenv("PENZU",alt))
continueDay()

# notion
printMessage("Check your calendar")
printMessage("Update Daily Tasks")
webbrowser.open_new_tab(os.getenv("NOTION",alt))
continueDay()

# start touch type measure and practice
printMessage("test 1")
webbrowser.open(os.getenv("TEST1",alt))
continueDay()
printMessage("test 2")
webbrowser.open(os.getenv("TEST2",alt))
continueDay()
printMessage("test 3")
webbrowser.open(os.getenv("TEST3",alt))
continueDay()
printMessage("test 4")
webbrowser.open(os.getenv("TEST4",alt))
continueDay()

# cal & update daily type progess
printMessage("WPM daily update")
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
webbrowser.open(os.getenv("T_WORKSHEET",alt))
continueDay()

# anki
printMessage("Anki time!")
webbrowser.open(os.getenv("ANKI"),alt)
continueDay()

# mail
printMessage("Check mail")
webbrowser.open(os.getenv("MAIL",alt))
continueDay()

# whatsapp
printMessage("Check whatsapp")
# sendNotificationOnWindows("Open Whatsapp")
webbrowser.open(os.getenv("WHATSAPP",alt))
continueDay()

# leetcode
printMessage("DSA Practice")
webbrowser.open(os.getenv("LEETCODE",alt))
continueDay()

printMessage("Let's take a bread!")
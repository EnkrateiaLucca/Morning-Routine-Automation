import webbrowser
import time
import os
import subprocess
from datetime import datetime
from plyer import notification


'''
Utility functions
'''
def sendNotificationOnLinux(message):
    subprocess.Popen(["notify-send", message])
    return

def sendNotificationOnWindows(title, message, app_image=None):
    # check fo rimage to be .ico file
    notification.notify(
        title = title,
        message = message,
        app_icon = app_image,
        timeout = 10,
    )
# def sendNotificationOnWindows(msg="", delay=2):
#     t = 0
#     notify = ToastNotifier()
#     while t < delay:
#         notify.show_toast("Notification",msg)
#         time.sleep(1)
#         t+=1

def continueDay():
    cont = input("Press ENTER too continue")
    # sendNotificationOnWindows("continue","CONTINUE?")

'''
Start here
'''
os.system("bash logSystemOnOff.sh") 

# # sendNotificationOnWindows("How was the workout? Share with Penzu")
# print("How was the workout? Share with Penzu")
# webbrowser.open("https://penzu.com/journals/25285684/new")
# continueDay()

# # notion
# print("Check your calendar")
# print("Update Daily Tasks")
# webbrowser.open_new_tab("www.notion.so")
# continueDay()

# # start touch type measure and practice
# print("test 1")
# webbrowser.open("https://10fastfingers.com/typing-test/english")
# continueDay()
# print("test 2")
# webbrowser.open("https://10fastfingers.com/top1000")
# continueDay()
# print("test 3")
# webbrowser.open("https://typetest.io/")
# continueDay()
# print("test 4")
# webbrowser.open("https://www.keybr.com/")
# continueDay()

# cal & update daily type progess
print("WPM daily update")
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
webbrowser.open("https://docs.google.com/spreadsheets/d/1q3SI5mlltNWSbDY8oEg-ID4EAzzs0jBEX7uA-BCHkNQ/edit#gid=0")
continueDay()

# anki
print("Anki time!")
webbrowser.open("https://ankiweb.net/decks/")
continueDay()

# mail
print("Check mail")
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
continueDay()

# whatsapp
print("Check whatsapp")
# sendNotificationOnWindows("Open Whatsapp")
webbrowser.open("https://web.whatsapp.com/")
continueDay()

# leetcode
print("DSA Practice")
webbrowser.open("https://leetcode.com/problem-list/3d1b6ab26e9d4b5bbc663aaa1010f252/?sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkRJRkZJQ1VMVFkifV0%3D&page=1")
continueDay()

print("Let's take a bread!")



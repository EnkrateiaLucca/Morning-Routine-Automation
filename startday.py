import webbrowser
import time
import os
import subprocess
from datetime import datetime


def sendNotificationOnLinux(message):
    subprocess.Popen(["notify-send", message])
    return


def sendNotificationOnWindows(msg="", delay=2):
    t = 0
    notify = ToastNotifier()
    while t < delay:
        notify.show_toast("Notification",msg)
        time.sleep(1)
        t+=1

def continueDay():
    cont = input("Press too continue")


os.system("bash logSystemOnOff.sh") 

print("Run keyfrequency and active window loggers with sudo")

# clockify
print("Turn on Focus")
continueDay()

print("Turn on white noise")
continueDay()

# Google calendar events
print("Check your calendar")
webbrowser.open("https://calendar.google.com/calendar/u/0/r/day")


# notion 
webbrowser.open_new_tab("www.notion.so")
print("Write your todo list on the Notion table with the routine and the specifics")
continueDay()


# start vscode for coding
print("TYPE")
os.system('"mlt random "0)-_=+[{]};:\'\|//?"')
os.system("mlt random 123456!@#$%^qwertasdfgzxcvbZXCVBASDFGQWERT~")
os.system("python /home/lucassoares/Desktop/automated/logTyping.py")
continueDay()


print("MANDARIN")
webbrowser.open("www.duolingo.com")
continueDay()

print("CODE")
webbrowser.open("https://projecteuler.net/archives")
# start Anki


# mail
# teams, mail, slack, whatsapp
sendNotificationOnLinux("Open Mail, Teams, Slack and Whatsapp")
os.system("teams")
os.system("mailspring")
os.system("slack")
webbrowser.open("https://web.whatsapp.com/")

# medium
webbrowser.open("https://medium.com/me/partner/dashboard")
print("Check your stats on Medium")
continueDay()

print("Leave an Ipython window open!")

print("Be greateful, no negative thoughts and have a great day!")



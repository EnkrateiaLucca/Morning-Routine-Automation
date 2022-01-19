from plyer import notification
import subprocess



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

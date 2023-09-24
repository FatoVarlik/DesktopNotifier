import plyer
from plyer import notification

notification_title = "Desktop Notifier"
notification_message = "Notification sent successfully."

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 5,
    toast = False
)
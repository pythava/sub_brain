from plyer import notification

def notice(title, message, app_name, timeout):
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
        timeout=timeout
    )
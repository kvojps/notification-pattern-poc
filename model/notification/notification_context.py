from model.notification.notification import Notification


class NotificationContext():
    def __init__(self):
        self._notifications = []

    def add_notification(self, notification: Notification):
        self._notifications.append(notification)

    def get_errors(self):
        return [notification.to_dict() for notification in self._notifications]

    def has_errors(self):
        return len(self._notifications) > 0

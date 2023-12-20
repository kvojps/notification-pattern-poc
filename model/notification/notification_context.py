from pydantic import BaseModel
from typing import List

from model.notification.notification import Notification


class NotificationContext(BaseModel):
    _notifications: List[Notification]

    def __init__(self):
        super().__init__()

    def add_notification(self, notification: Notification):
        self._notifications.append(notification)

    def has_errors(self):
        return len(self._notifications) > 0

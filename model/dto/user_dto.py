from pydantic import BaseModel

from model.notification.notification import Notification
from model.notification.notification_context import NotificationContext


class UserDTO(BaseModel):
    notification_context: NotificationContext
    name: str
    email: str
    cpf: str
    age: int

    def __init__(self):
        super().__init__()
        self.validate()

    def _validate(self):
        self._validate_name()
        self._validate_email()
        self._validate_cpf()
        self._validate_age()

    def _validate_name(self):
        if len(self.name) < 4:
            self.notification_context.add_notification(
                Notification("Invalid name",
                             "Name must have at least 4 characters")
            )

    def validate_email(self):
        if "@" not in self.email:
            self.notification_context.add_notification(
                Notification("Invalid email",
                             "Email must have @")
            )

    def _validate_cpf(self):
        if len(self.cpf) != 11:
            self.notification_context.add_notification(
                Notification("Invalid CPF",
                             "CPF must have 11 characters")
            )

    def _validate_age(self):
        if self.age < 18:
            self.notification_context.add_notification(
                Notification("Invalid age",
                             "Age must be greater than 18")
            )

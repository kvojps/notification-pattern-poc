from pydantic import BaseModel

from model.notification.notification import Notification
from model.notification.notification_context import NotificationContext


class UserDTO():
    def __init__(self, name: str, email: str, cpf: str, age: int):
        self._notification_context = NotificationContext()
        self._name = name
        self._email = email
        self._cpf = cpf
        self._age = age

        self._validate()

    def get_notification_context(self):
        return self._notification_context

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf

    def get_age(self):
        return self._age

    def _validate(self):
        self._validate_name()
        self._validate_email()
        self._validate_cpf()
        self._validate_age()

    def _validate_name(self):
        if len(self._name) < 4:
            self._notification_context.add_notification(
                Notification("Invalid name",
                             "Name must have at least 4 characters")
            )

    def _validate_email(self):
        if "@" not in self._email:
            self._notification_context.add_notification(
                Notification("Invalid email",
                             "Email must have @")
            )

    def _validate_cpf(self):
        if len(self._cpf) != 11:
            self._notification_context.add_notification(
                Notification("Invalid CPF",
                             "CPF must have 11 characters")
            )

    def _validate_age(self):
        if self._age < 18:
            self._notification_context.add_notification(
                Notification("Invalid age",
                             "Age must be greater than 18")
            )

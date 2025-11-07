# Задание №2

from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send(self, message, recipient):
        pass



class EmailSender(NotificationSender):
    def __init__(self):

        self._service = "Gmail"



    def send(self, message, recipient):
        return f"Email sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"


class SmsSender(NotificationSender):
    def __init__(self):

        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"


class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"







email = EmailSender()

print(email.send("Привет", "john@mail.ru"))
print(email.get_service())


sms = SmsSender()

print(sms.send("Hi!", "+123456789"))
print(sms.get_service())

push = PushSender()
print(push.send("Hello!", "User123"))
print(push.get_service())







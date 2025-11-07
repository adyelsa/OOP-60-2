# Задание №3


import random
from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance

        self.__password = password

    def get_balance(self, password):

        if password == self.__password:
            return self._balance

        return "Неверный пароль!"


    def withdraw(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        if amount > self._balance:
            return "Недостаточно средствв!"

        self._balance -= amount
        return self._balance


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


class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username

        self.account = account
        self.notifier = notifier

    def login(self, password):
        if isinstance(self.account.get_balance(password), (int, float)):
            print(self.notifier.send(f"Успешный вход: {self.username}", "любой_номер_или_почта"))
            return True


        return False


    def transfer(self, amount, password, recipient_account: BankAccount):
        if isinstance(self.account.get_balance(password), (int, float)):
            result = self.account.withdraw(amount, password)
            if isinstance(result, str):
                return result
            recipient_account._balance += amount
            print(self.notifier.send(f"Перевод {amount} отправлен", "любой_номер_или_почта"))
            print(self.notifier.send(f"Получено {amount} от {self.username}", "любой_номер_или_почта"))
            return True
        return "Неверный пароль!"




john = BankAccount("John", 200, "secret")

alice = BankAccount("Alice", 50, "pass123")
notifier = SmsSender()

auth = UserAuth("john_doe", john, notifier)


print("Логин:", auth.login("secret"))

auth.transfer(70, "secret", alice)

print("John:", john.get_balance("secret"))
print("Alice:", alice.get_balance("pass123"))







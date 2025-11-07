# Задание №1


import random

class BankAccount:

    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance

        self.__password = password

    def deposit(self, amount, password):

        if password == self.__password:
            self._balance += amount
            return self._balance

        return "Неверный пароль!"

    def withdraw(self, amount, password):
        if password != self.__password:

            return "Неверный пароль!"
        if amount > self._balance:
            return "Недостаточн средств!"
        self._balance -= amount
        return self._balance
    def change_password(self, old_password, new_password):
        if old_password == self.__password:

            self.__password = new_password
            return "Пароль изменён"
        return "Старый пароль неверный"




    def get_balance(self, password):
        if password == self.__password:
            return self._balance

        return "Неверный пароль !"

    def reset_pin(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin

    def __generate_pin(self):
        return str(random.randint(1000, 9999))



john = BankAccount("John", 100, "123qwerty")

print("Пополнение:", john.deposit(50, "123qwerty"))        # 150

print("Снятие:", john.withdraw(200, "123qwerty"))          # Недостаточно средств!
print("Баланс:", john.get_balance("123qwerty"))            # 150
print("Смена пароля:", john.change_password("wrong", "new"))# Старый пароль неверный
new_pin = john.reset_pin("123qwerty")

print("Новый PIN:", new_pin)

print("Баланс с новым PIN:", john.get_balance(new_pin))     # 150
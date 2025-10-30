# Домашнее задание №1

class Car:
    def __init__(self, brand, color, speeed):
        self.brand = brand
        self.color = color
        self.speed = speeed


    def description(self):
        return f"Марка: {self.brand}, Цвет: {self.color}, Скорость: {self.speed} км/ч"

    def accelerate(self, value):
        self.speed += value

        print(f"{self.brand} ускорились на {value} км/ч и теперь скорость {self.speed} км/ч.")


car1 = Car("Mercedes", "черный", 180)
car2 = Car("BMW", "синий", 160)



print(car1.description())
print(car2.description())

car1.accelerate(20)
car2.accelerate(40)




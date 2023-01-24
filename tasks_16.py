# 16.7.1
class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


# 16.8.1, 16.8.2
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2


pi = 3.14
class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return pi * self.r ** 2


# 16.9.1, 16.9.2
class Rectangle_x_y:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"
    def get_area(self):
        return (self.height * self.width)


# 16.9.3, 16.9.4
class Client:
    def __init__(self, firstname, lastname, city, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"{self.firstname} {self.lastname}. {self.city}. Баланс: {self.balance} руб."
    def clients_list(self):
        return f"{self.firstname} {self.lastname}, {self.city}"


# 16.10.5
class SquareException(Exception):
   pass


class NonPositiveDigitException(ValueError):
    pass


class Square_x:
    def __init__(self, x):
        self.x = x
        if x <= 0:
            raise NonPositiveDigitException("Недопустимое значение стороны квадрата, 'х' должен быть > 0.")
    def get_area_square_x(self):
        return self.x ** 2

square1 = Square_x(-2)
print(square1.get_area_square_x())

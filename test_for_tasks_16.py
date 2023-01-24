# 16.7.1
from tasks_16 import Cat

cat1 = Cat('Семён', 'мальчик', 5)
print('cat1.name= ', cat1.name)
print('cat1.gender= ', cat1.gender)
print('cat1.age= ', cat1.age)

cat2 = Cat('Васька', 'девочка', 1)
print('\ncat2.name= ', cat2.name)
print('cat2.gender= ', cat2.gender)
print('cat2.age= ', cat2.age)
print()

# 16.8.1, 16.8.2
from tasks_16 import Rectangle,Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_area())
print(rect2.get_area())

square1 = Square(5)
square2 = Square(10)
print(square1.get_area_square(),
      square2.get_area_square())

circle1 = Circle(10)
circle2 = Circle(3)
print(circle1.get_area_circle(),
      circle2.get_area_circle())

figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
print()

# 16.9.1, 16.9.2
from tasks_16 import Rectangle_x_y

rectangle1 = Rectangle_x_y(5, 10, 50, 100)
print(rectangle1)
print(rectangle1.get_area())
print()

# 16.9.3,16.9.4
from tasks_16 import Client

client1 = Client('Иван', 'Петров', 'Москва', 50)
print(client1)
print()

client2 = Client('Сидор', 'Сидоров', 'Баку', 30)
client3 = Client('Василий', 'Иванов', 'Екатеринбург', 5)

list1 = [client1, client2, client3]
for client in list1:
    print(client.clients_list())
print()

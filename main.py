"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін

  ###############################################################################
"""
from typing import Self


class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y

    def __add__(self, other: Self):
        return f'Add: {self.square() + Rectangle.square(other)}'

    def __sub__(self, other: Self):
        return f'Sub: {self.square() - Rectangle.square(other)}'

    def __eq__(self, other: Self):
        return f'Equal: {self.square() == Rectangle.square(other)}'

    def __lt__(self, other: Self):
        return f'Lt: {self.square() < Rectangle.square(other)}'

    def __gt__(self, other: Self):
        return f'Gt: {self.square() > Rectangle.square(other)}'

    def __ne__(self, other: Self):
        return f'Ne: {self.square() != Rectangle.square(other)}'

    def __len__(self):
        return 2 * (self.x + self.y)

    def __str__(self):
        return f'Square: {self.square()}'


rect1 = Rectangle(4, 5)
rect2 = Rectangle(5, 9)

print(f'Rect1: {rect1}')
print(f'Rect2: {rect2}')

print(rect2 + rect1)
print(rect2 - rect1)
print(rect2 == rect1)
print(rect2 < rect1)
print(rect2 > rect1)
print(rect2 != rect1)

print(f'Perimeter rect1: {len(rect1)}')
print(f'Perimeter rect2: {len(rect2)}')

print('-' * 50)
"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення


###############################################################################
"""


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Prince(Human):
    def __init__(self, name: str, age: int, size_shoe: int):
        super().__init__(name, age)
        self.size_shoe = size_shoe

    def find_cinderella(self, *args: str | int):
        for size in args:
            if size == self.size_shoe:
                print(f'Is size: {size} perfect! {args[1]} is Cinderella!!!')

    def __str__(self):
        return f'I"m Prince, my name is {self.name}, my {self.age} years old, ' \
               f'and I found a size {self.size_shoe} shoe.'


class Cinderella(Human):
    count: int = 0

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size
        Cinderella.count += 1
        self.number = Cinderella.count

    def __str__(self):
        return f'My name is {self.name}, my {self.age} years old, ' \
               f'I have shoe size {self.size} and my number {self.number}. ' \
               f'All instances: {self.count}.'


girls = [
    Cinderella('Tonya', 70, 45),
    Cinderella('Nina', 70, 48),
    Cinderella('Valera', 77, 46),
    Cinderella('Polina', 80, 44)
]

prince = Prince('Fedya', 77, 44)

print(prince)
[print(girl) for girl in girls]
[prince.find_cinderella(girl.size, girl.name) for girl in girls]

print('-' * 50)
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print('Book: ', self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print('Magazine: ', self.name)


"""
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

Приклад:

Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
    

для перевірки ксассів використовуємо метод isinstance, приклад:


user = User('Max', 15)
shape = Shape()

isinstance(max, User) -> True
isinstance(shape, User) -> False
"""


class Main:
    printable_list: list = []

    @classmethod
    def add(cls: Self, instance: object) -> None:
        if isinstance(instance, (Book, Magazine)):
            cls.printable_list.append(instance)

    @classmethod
    def show_all_magazines(cls) -> None:
        for instance in cls.printable_list:
            if isinstance(instance, Magazine):
                instance.print()

    @classmethod
    def show_all_books(cls) -> None:
        for instance in cls.printable_list:
            if isinstance(instance, Book):
                instance.print()


main = Main()
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

"""
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
_________________________________________________________________________
    Задание 9.3
    Создать класс Animal, который будет содержать информацию о животном.
    Класс должен иметь следующие атрибуты:
        - имя
        - возраст
    Класс должен иметь метод make_sound(), который будет выводить в консоль звук, который издает животное.
    Создать несколько классов-наследников Animal и реализовать для каждого из них метод make_sound().
    Создать класс Zoo, который будет содержать информацию о зоопарке.
    Класс должен иметь следующие атрибуты:
        - список животных
        - список сотрудников
    Класс должен иметь методы:
        - добавить животное в список
        - добавить сотрудника в список
        - сохранить информацию о зоопарке в файл
        - загрузить информацию о зоопарке из файла
"""

import json


# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")


# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} is chirping.")


# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} is roaring.")


# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} is hissing.")


# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс Zoo  (Композиция Zoo, Animal, Employee)
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            "animals": [{"name": animal.name, "age": animal.age} for animal in self.animals],
            "employees": [{"name": employee.name, "role": employee.role} for employee in self.employees]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    # Обновленный метод load_from_file
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.animals = [Animal(animal['name'], animal['age']) for animal in data['animals']]
            self.employees = []
            for emp_data in data['employees']:
                if emp_data['role'] == "Zoo Keeper":
                    self.employees.append(ZooKeeper(emp_data['name'], emp_data['role']))
                elif emp_data['role'] == "Veterinarian":
                    self.employees.append(Veterinarian(emp_data['name'], emp_data['role']))


# Класс Employee
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role


# Подкласс ZooKeeper
class ZooKeeper(Employee):
    def __init__(self, name, role="Zoo Keeper"):
        super().__init__(name, role)
        self.role = role

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")


# Подкласс Veterinarian
class Veterinarian(Employee):
    def __init__(self, name, role="Veterinarian"):
        super().__init__(name, role)
        self.role = role

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# Пример использования
# Создание зоопарка
zoo = Zoo()

# Загрузка зоопарка из файла (Десериализация)
zoo.load_from_file("zoo_data1.json")


# Добавление животных
zoo.add_animal(Bird("Tweety_4", 32))
zoo.add_animal(Bird("Robin", 3))
zoo.add_animal(Mammal("Lion_4", 25))
zoo.add_animal(Reptile("Snake_4", 23))

# Добавление сотрудников
zoo.add_employee(ZooKeeper("Tom_3", "Zoo Keeper"))
zoo.add_employee(Veterinarian("Jerry_3", "Veterinarian"))

# Полиморфизм
animals = zoo.animals
animal_sound(animals)

# Использование методов сотрудников
for employee in zoo.employees:
    if isinstance(employee, ZooKeeper):
        employee.feed_animal(zoo.animals[2])
    elif isinstance(employee, Veterinarian):
        employee.heal_animal(zoo.animals[3])

# Сохранение зоопарка в файл (Сериализация)
zoo.save_to_file("zoo_data1.json")

"""Менеджер задач
Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
    описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
    отметки выполненных задач и вывода списка текущих (не выполненных) задач.

*Дополнительное задание:

Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.

Шаги:

1. Создай класс `Store`:

-Атрибуты класса:

- `name`: название магазина.

- `address`: адрес магазина.

- `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.

- Методы класса:

- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.

-  метод для добавления товара в ассортимент.

- метод для удаления товара из ассортимента.

- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.

- метод для обновления цены товара.

2. Создай несколько объектов класса `Store`:

Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.

3. Протестировать методы:

Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.
"""
class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_completed(self):
        self.status = True

    def __str__(self):
        return f"Task: {self.description}, Deadline: {self.deadline}, Status: {'Выполнена' if self.status else 'Не выполнена'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_incompleted_tasks(self):
        return [task for task in self.tasks if not task.status]

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status]

    def mark_task_as_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_as_completed()
                break

# *Дополнительное задание:
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

# метод для добавления товара в ассортимент.
    def add_item(self, item_name, price):
        self.items[item_name] = price

# метод для удаления товараиз ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

# метод для получения цены товара по его названию.Если товар отсутствует, возвращайте `None`.
    def get_price(self, item_name):
        return self.items.get(item_name)

# метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Пример использования:

# Менеджер задач
# Создание задач
task1 = Task("Пройти тему Введение в ООП", "2025-08-10")
task2 = Task("Завершить полный курс", "2025-12-28")

# Создание менеджера задач
task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)

# Вывод списка невыполненных задач
print("Невыполненные задачи:")
for task in task_manager.list_incompleted_tasks():
    print(task)

# Отметка задачи как выполненной
task_manager.mark_task_as_completed("Пройти тему Введение в ООП")

# Вывод списка невыполненных задач после отметки
print("Невыполненные задачи после отметки выполненных:")
for task in task_manager.list_incompleted_tasks():
    print(task)

# Вывод списка выполненных задач
print("Выполненные задачи:")
for task in task_manager.list_completed_tasks():
    print(task)


# Программное обеспечение для сети магазинов
# Создание объектов класса Store
store1 = Store("Светотехника", "Светлая, 1")
store2 = Store("Люстры Супер", "Суперская, 999")
store3 = Store("Дешевый Светик", "Мерзкая, 666(подвал)")

# Добавление товаров в магазины
store1.add_item("Лампа настольная светодиолная", 2500)
store1.add_item("Торшер Крутой", 6000)
store2.add_item("Люстра Хрустальная 20 галогенных ламп", 37000)
store3.add_item("Лампы светодиодные НОНЕЙМ", 50)

# Тестирование методов
print(store1.get_price("Лампа настольная светодиолная"))  # Вывод: 2500
store1.update_price("Лампа настольная светодиолная", 2750)
print(store1.get_price("Лампа настольная светодиолная"))  # Вывод: 2750
store1.remove_item("Торшер Крутой")
print(store1.get_price("Торшер Крутой"))  # Вывод: None

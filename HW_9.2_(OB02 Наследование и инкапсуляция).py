"""
Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
 Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
  пользователя из системы.

Требования:

1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных
сотрудников).

2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный
 для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять
 и удалять пользователей из списка (представь, что это просто список экземпляров User).

3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь
доступ к необходимым атрибутам через методы (например, get и set методы).
"""


class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    # аналог info, только в одну строку. выводит значения всех полей объекта класса командой print
    def __str__(self):
        return f"User ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user_id):
        self.__users = [user for user in self.__users if user.get_user_id() != user_id]

    def list_users(self):
        return self.__users

    # аналог info, только в одну строку. выводит значения всех полей  объекта класса командой print
    def __str__(self):
        return f"Admin ID: {self.get_user_id()}, Name: {self.get_name()}, Access Level: {self.get_access_level()}"

# Пример использования

# Создание пользователей
user1 = User(1, "Вася Пупкин")
user2 = User(2, "Робот Производительный")

# Создание администратора
admin = Admin(3, "Иван Боссов")
print(f"Создан администратор: {admin}\n")

# Добавление пользователей
admin.add_user(user1)
admin.add_user(user2)

# Вывод списка пользователей
print("Список сотрудников(не явяющихся администраторами):")
for user in admin.list_users():
    print(user)

# Удаление пользователя
admin.remove_user(1)

# Вывод списка пользователей после удаления
print("\nСписок сотрудников(не явяющихся администраторами)  после Удаления пользователя:")
for user in admin.list_users():
    print(user)

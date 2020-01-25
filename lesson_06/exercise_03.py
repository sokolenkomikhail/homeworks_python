'''Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).'''

# Есть сомнения по поводу правильности моего решения. Слишком размытые условия


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        my_dict = {'wage': 35000, 'bonus': 15000}
        self._income = my_dict.get('wage') + my_dict.get('bonus')


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        return self._income


b = Position('Василий', 'Пупкин', 'Менеджер')
print(b.name)
print(b.surname)
print(b.position)

b.get_full_name()
print(b.get_total_income())

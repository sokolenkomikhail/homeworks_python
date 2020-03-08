'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.'''
'''Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.'''
'''Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.'''

from abc import abstractmethod


class Warehouse:

    @abstractmethod
    def to_take(self, quantity):
        pass

    @abstractmethod
    def to_give(self, quantity, department):
        pass


class OfficeEquipment(Warehouse):
    _item_list = []                             # В списке хранятся словари для каждого экземпляра класса
    index = -1                                  # Индекс для получения/изменения словаря для каждого экземпляра

    def __init__(self, title):
        self.title = title

    def to_take(self, qty):
        try:
            self._item_list[self.index]['Количество'] = self._item_list[self.index].get('Количество') + qty
            print(f'Принято {qty} {self.title} на склад')
        except TypeError:
            print('Некорректные параметры!')

    def to_give(self, qty, department):
        try:
            if self._item_list[self.index].get('Количество') < qty:
                print(f'Недостаточное количество {self.title} на складе!')
            else:
                self._item_list[self.index]['Количество'] = self._item_list[self.index].get('Количество') - qty
                print(f'Передано {qty} {self.title} в {department}')
        except TypeError:
            print('Некорректные параметры!')

    def get_info(self):
        print(self._item_list[self.index])


class Printer(OfficeEquipment):
    _item_list = []
    index = -1

    def __init__(self, title, param):
        super().__init__(title)
        self.dict = {'Название': self.title, 'Цветность печати': param, 'Количество': 0}
        self._item_list.append(self.dict)
        Printer.index += 1
        self.index = Printer.index


class Scanner(OfficeEquipment):
    _item_list = []
    index = -1

    def __init__(self, title, param):
        super().__init__(title)
        self.dict = {'Название': self.title, 'Тип сканера': param, 'Количество': 0}
        self._item_list.append(self.dict)
        Scanner.index += 1
        self.index = Scanner.index


class CopyMachine(OfficeEquipment):
    _item_list = []
    index = -1

    def __init__(self, title, param, param2):
        super().__init__(title)
        self.dict = {'Название': self.title, 'Цветность печати': param, 'Тип сканера': param2, 'Количество': 0}
        self._item_list.append(self.dict)
        CopyMachine.index += 1
        self.index = CopyMachine.index


a = Printer('HP', 'Цветной')
b = Printer('Brother', 'ЧБ')
c = Printer('Canon', 'Цветной')
d = Scanner('HP', 'планшетный')
e = Scanner('Xerox', 'планшетный')
f = CopyMachine('Xerox', 'ЧБ', 'планшетный')

a.to_take(7)
b.to_take(10)
c.to_take(4)
d.to_take(8)
e.to_take(5)
f.to_take(8)

a.get_info()
b.get_info()
c.get_info()
d.get_info()
e.get_info()
f.get_info()

a.to_give(6, 'отдел маркетинга')
b.to_give(5, 'бухгалтерия')
c.to_give(2, 'отдел рекламы')

a.get_info()
b.get_info()
c.get_info()

'''Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.'''


class Cell:
    def __init__(self, quantity):
        self.qty = quantity

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        return Cell(self.qty - other.qty) if self.qty > other.qty else 'Разность меньше нуля!'

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    def __str__(self):
        return f'Клетка с {self.qty} ячейками'

    def make_order(self, cell_in_lines):
        self.line = cell_in_lines
        return ''.join('*'*self.line + '\n' for i in range(self.qty // self.line)) + ''.join('*'*(self.qty % self.line))


cell_1 = Cell(17)
print(cell_1)
print(cell_1.make_order(5))

cell_2 = Cell(12)
print(cell_2)
print(cell_2.make_order(5))

cell_3 = cell_1 + cell_2
print(cell_3)
print(cell_3.make_order(5))

cell_4 = cell_1 - cell_2
print(cell_4)
print(cell_4.make_order(5))

cell_5 = cell_1 * cell_2
print(cell_5)
print(cell_5.make_order(25))

cell_6 = cell_1 / cell_2
print(cell_6)
print(cell_6.make_order(5))

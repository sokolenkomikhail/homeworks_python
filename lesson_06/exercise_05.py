'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Рисуем карандашом', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Пишем ручкой', self.title)


class Handle(Stationery):
    def draw(self):
        print('Размечаем маркером', self.title)


a = Pen('<pen_title>')
b = Pencil('<pencil_title>')
c = Handle('<handle_title>')

a.draw()
b.draw()
c.draw()

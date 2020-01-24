'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.'''

import time


class TrafficLight:
    def __init__(self):
        self.__color = None
        self.count = 0                                  # счетчик прикручен для проверки порядка сигналов

    def running(self, color):
        self.__color = color
        light_list = ['red', 'yellow', 'green']         # лист для проверки порядка
        if self.count > 2:
            self.count = self.count % 3                 # переназначение count по условию (не выйти за пределы списка)
        if str(self.__color).lower() == light_list[self.count]:     # проверка порядка по условию
            print(light_list[self.count].title() + '...')
            self.count += 1
            if self.__color.lower() == 'red':
                time.sleep(7)
            elif self.__color.lower() == 'yellow':
                time.sleep(2)
            else:
                time.sleep(5)
        else:                                           # если порядок нарушен, либо некорректные данные
            if str(self.__color).lower() in light_list:
                print('Incorrect sequence!')
            else:
                print('Incorrect argument!')


a = TrafficLight()

a.running('red')
a.running('YELLOW')
a.running('green')
a.running('red')
a.running('yellow')
a.running('Red')
a.running('green')
a.running(1)

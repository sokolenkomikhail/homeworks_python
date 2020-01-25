'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.speed_limit = 60                       # установил базовое ограничение по скорости
        self.is_police = False

    def go(self):
        print(self.color.title(), self.name, 'went')

    def stop(self):
        print(self.color.title(), self.name, 'stopped')

    def turn(self, direction):
        if direction.lower() == 'right':
            print(self.color.title(), self.name, 'turned right')
        elif direction.lower() == 'left':
            print(self.color.title(), self.name, 'turned left')
        else:
            print('Incorrect argument!')

    def showspeed(self):
        print(f'Vehicle speed {self.speed} kmph')


class TownCar(Car):
    def showspeed(self):
        if self.speed > self.speed_limit:
            print(f'Over speed!\nVehicle speed {self.speed} kmph')
        else:
            print(f'Vehicle speed {self.speed} kmph')


class SportCar(Car):
    def get_car_info(self):
        print('It is a sport car')


class WorkCar(TownCar):                             # по условию наследование дб от класса Car. Сделал наследование от
    def __init__(self, speed, color, name):         # класса TownCar, чтобы избежать дублирования кода для showspeed
        super().__init__(speed, color, name)
        self.speed_limit = 40                       # переназначил ограничение по скорости


class PoliceCar(Car):
    def __init__(self, speed):
        super().__init__(speed, color='blue', name='Police car')
        self.is_police = True

# ниже дополнительно добавил классы: Пожарная машина и Скорая помощь


class FireEngine(Car):
    def __init__(self, speed):
        super().__init__(speed, color='red', name='Fire engine')


class Ambulance(Car):
    def __init__(self, speed):
        super().__init__(speed, color='white', name='Ambulance')


# Вызов методов

first_car = TownCar(61, 'silver', 'Prius')
first_car.go()
first_car.stop()
first_car.turn('right')
first_car.turn('left')
first_car.showspeed()
print(first_car.is_police)

second_car = SportCar(190, 'red', 'McLaren F1')
second_car.get_car_info()
second_car.go()
second_car.stop()
second_car.turn('right')
second_car.turn('left')
second_car.showspeed()
print(second_car.is_police)

third_car = WorkCar(42, 'yellow', 'Komatsu')
third_car.go()
third_car.stop()
third_car.turn('right')
third_car.turn('left')
third_car.showspeed()
print(third_car.is_police)

fourth_car = PoliceCar(89)
fourth_car.go()
fourth_car.stop()
fourth_car.turn('right')
fourth_car.turn('left')
fourth_car.showspeed()
print(fourth_car.is_police)

fifth_car = FireEngine(62)
fifth_car.go()
fifth_car.stop()
fifth_car.turn('right')
fifth_car.turn('left')
fifth_car.showspeed()
print(fifth_car.is_police)

sixth_car = Ambulance(73)
sixth_car.go()
sixth_car.stop()
sixth_car.turn('right')
sixth_car.turn('left')
sixth_car.showspeed()
print(sixth_car.is_police)

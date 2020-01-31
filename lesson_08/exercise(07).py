'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class Complex:
    def __init__(self, re, im):
        self.re = re                            # Вещественная часть
        self.im = im                            # Мнимая часть

    def __str__(self):                          # Перегрузка __str__ для привычного вывода
        if self.re != 0 and self.im > 0:
            return f'{self.re} + {self.im}i'
        elif self.re != 0 and self.im < 0:
            return f'{self.re} - {abs(self.im)}i'
        elif self.re != 0 and self.im == 0:
            return str(self.re)                 # вещественное число
        elif self.re == 0 and self.im != 0:
            return str(self.im) + 'i'           # мнимое число
        else:
            return '0'                          # комплексный ноль

    def __add__(self, other):
        return Complex((self.re + other.re), (self.im + other.im))

    def __mul__(self, other):
        return Complex((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))


a = Complex(2, 5)
print(a)
b = Complex(3, 4)
print(b)
print(a + b)
print(a * b)

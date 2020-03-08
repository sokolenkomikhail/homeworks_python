'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.'''


class ZeroInput(Exception):
    def __init__(self, text):
        self.text = text


class NaN(Exception):
    def __init__(self, text):
        self.text = text


a = input('Insert the dividend: ')
b = input('Insert the divider (not equal to zero): ')
try:
    if not a.isdigit() or not b.isdigit():
        raise NaN('Not a Number')
    elif int(b) == 0:
        raise ZeroInput('Zero input')
    else:
        print(f'Result = {int(a) / int(b)}')
except NaN:
    print('Not a number(s)!')
except ZeroInput:
    print('Division by zero!')

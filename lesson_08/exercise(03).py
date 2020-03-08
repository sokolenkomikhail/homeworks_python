'''Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.'''


class NaN(Exception):
    def __init__(self, text):
        self.text = text


num_list = []

while True:
    try:
        usr_input = input('Insert the number: ')
        if usr_input.isdigit():
            num_list.append(int(usr_input))
        elif usr_input.lower() == 'stop':
            print(num_list)
            break
        else:
            raise NaN('Not a Number')
    except NaN:
        print('Not a number!')

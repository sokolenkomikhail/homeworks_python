'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('text_01.txt', 'w') as f_obj:
    while True:
        usr_input = input('Введите строку: ')
        if usr_input == '':
            break
        else:
            print(usr_input, file=f_obj)

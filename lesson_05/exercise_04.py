'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Zero': 'Ноль'
           }

with open('text_04.txt') as f_obj:
    my_list = [my_dict.get(item.split()[0]) + ' — ' + item.split()[-1] + '\n' for item in f_obj.readlines()]

print(my_list)

with open('text_04-2.txt', 'w') as n_obj:
    n_obj.writelines(my_list)

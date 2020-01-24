'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

my_list = [1, 2, 4, 6, 1, 43, 89, 3, 11, 45, 12, 83]

with open('text_05.txt', 'w') as f_obj:
    for el in my_list:
        f_obj.write(str(el) + ' ')

with open('text_05.txt', 'r') as f_obj:
    new_list = [int(el) for el in f_obj.read().split()]

print(sum(new_list))

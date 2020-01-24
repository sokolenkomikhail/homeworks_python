'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.'''

def my_func(my_str):
    my_list = []
    for i in range(len(my_str.split())):
        x = ''
        for el in my_str.split()[i]:
            if el.isdigit() == True:
                x += el
            else:
                break
        if x.isdigit():
            my_list.append(int(x))
    return sum(my_list)

with open('text_06.txt') as f_obj:
    lines = f_obj.readlines()

my_dict = {el.split(':')[0]: my_func(el.split(':')[1]) for el in lines}

print(my_dict)

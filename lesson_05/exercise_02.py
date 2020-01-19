'''Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''

with open('text_02.txt') as f_obj:
    lines = f_obj.readlines()
    for i, item in enumerate(lines):
        print(f'В {i + 1}-й строке: {len(item.split())} слов')

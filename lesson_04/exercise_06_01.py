'''Итератор, генерирующий целые числа, начиная с указанного.'''

from sys import argv

script_name, s_num = argv

from itertools import count

for i in count(int(s_num)):
    if i > 15:
        break
    else:
        print(i)
'''Итератор, повторяющий элементы некоторого списка, определенного заранее.'''

from sys import argv

script_name, f_num = argv

# Swaroop's Poetic Python from "A Byte of Python" by Swaroop C.H.
my_tuple = (
    "Programming is fun.",
    "When the work done,",
    "if you wanna make your work also fun:",
    "      use Python!",
    " "
)

from itertools import cycle

i = 0
for el in cycle(my_tuple):
    if i > int(f_num):
        break
    print(el)
    i += 1
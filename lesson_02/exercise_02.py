# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

user_list = []

el_qty = int(input("Введите количество элементов в списке: "))

for num_el in range(el_qty):
    user_el = input("Введите {}-й элемент списка: ".format(num_el + 1))
    user_list.append(user_el)

print(user_list)

n = 0
m = 1
while n < len(user_list) and m < len(user_list):
    user_list[n], user_list[m] = user_list[m], user_list[n]
    n += 2
    m += 2

print(user_list)
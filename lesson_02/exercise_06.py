# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Тут мне кажется, что я сильно загнался... Думаю, что можно было решить задачу при меньшем кол-ве строк.
qty = int(input("Введите количество товаров для внесения: "))

my_tuple = ('Название', 'Цена', 'Количество', 'Ед')
# Списки заполняются пользователем
name_list = []
price_list = []
qty_list = []
unit_list = []

for i in range(qty):
    name = input(f"Введите название товара {i + 1}: ")
    name_list.append(name)

    price = float(input(f"Введите цену на товар {i + 1}: "))
    price_list.append(price)

    prod_qty = int(input(f"Введите количество товара {i + 1}: "))
    qty_list.append(prod_qty)

    unit = input(f"Введите единицу измерения для товара {i + 1}(напр., шт): ")
    unit_list.append(unit)

# транспонирование списков
result_list = [name_list, price_list, qty_list, unit_list]
zip_list = zip(*result_list)
prod_list = list(zip_list)
# составление словаря с аналитикой
a_dict = {}
for a in range(len(my_tuple)):
    a_dict.setdefault(my_tuple[a], list(set(result_list[a])))
# составление списка словарей
dict_list = []
for n in range(len(prod_list)):
    prod_dict = {}
    for i in range(len(my_tuple)):
        prod_dict.setdefault(my_tuple[i], prod_list[n][i])
    dict_list.append(prod_dict)
# составление списка кортежей
tuple_list = []
for t in range(len(dict_list)):
    a = []
    a.append(t + 1)
    a.append(dict_list[t])
    b = tuple(a)
    tuple_list.append(b)
# вывод кортежей
for s in tuple_list:
    print(s)

print("Для вызова аналитики, введите 'A'.")
print("Для выхода введите 'Q'.")
user_input = None
while True:
    user_input = input("Ввод: ")
    if user_input.lower() == 'q':
        break
    elif user_input.lower() == 'a':
        for key, value in a_dict.items():
            print('{}: {}'.format(key, value))
    else:
        print("Некорректный ввод!")

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func(x, y):
    return x / y

arg_1 = int(input("Укажите делимое: "))

while True:
    arg_2 = int(input("Укажите делитель: "))
    if arg_2 == 0:
        print("Деление на ноль!")
    else:
        break

print(division_func(arg_1, arg_2))
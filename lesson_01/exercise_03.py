# -*- coding: utf-8 -*-

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = 0

while True:
    n = int(input("Введите число от 1 до 9: "))
    if n <= 9 and n > 0:
        break
    else:
        print("Недопустимое число!")

first_num = n
second_num = str(n) + str(n)
third_num = str(n) + str(n) + str(n)
sum = int(first_num) + int(second_num) + int(third_num)

result = "{} + {} + {} = {}".format(first_num, second_num, third_num, sum)

print(result)


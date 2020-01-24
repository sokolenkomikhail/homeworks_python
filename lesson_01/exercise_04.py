# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
#

user_num = 0

while True:
    user_num = int(input("Введите целое положительное число: "))
    if user_num <= 0:
        print("Недопустимый ввод!")
    else:
        break

result = max(str(user_num))

print(result)
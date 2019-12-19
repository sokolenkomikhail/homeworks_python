# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# Закоментировал еще одно решение. С ним код выглядит лаконичнее, но не знаю насколько такое решение уместно на данном этапе

total_seconds = int(input("Введите время в секундах: "))
total_minutes = total_seconds // 60

# seconds = str(total_seconds % 60).rjust(2, '0')
# minutes = str(total_minutes % 60).rjust(2, '0')
# hours = str(total_minutes // 60).rjust(2, '0')

seconds = total_seconds % 60
if seconds <= 9:
    seconds = "0{}".format(seconds)

minutes = total_minutes % 60
if minutes <= 9:
    minutes = "0{}".format(minutes)

hours = total_minutes // 60
if hours <= 9:
    hours = "0{}".format(hours)

print(hours, minutes, seconds, sep=':')
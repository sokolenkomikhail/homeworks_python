# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, byear, town, email, phone_number):
    print(name, surname, byear, town, email, phone_number, sep='/')

usr_name = input("Имя: ")
usr_surname = input("Фамилия: ")
usr_byear = input("Год рождения: ")
usr_town = input("Город: ")
usr_email = input("E-Mail: ")
usr_phone_number = input("Номер телефона: ")

my_func(name=usr_name, surname=usr_surname, byear=usr_byear, town=usr_town, email=usr_email, phone_number=usr_phone_number)
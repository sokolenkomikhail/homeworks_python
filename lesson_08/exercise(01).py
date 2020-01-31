'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

# Возможно, что я неправильно понял задание. Реализовал таким образом


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def cast(cls, date):
        return {'Day': int(date.split('-')[0]), 'Month': int(date.split('-')[1]), 'Year': int(date.split('-')[2])}

    @staticmethod
    def validation(date):
        day = Date.cast(date).get('Day')
        month = Date.cast(date).get('Month')
        year = Date.cast(date).get('Year')
        day_dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if month > 12:
            print('Некорректный месяц!')
        else:
            if month == 2 and ((year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28)):
                print('Некорректное число в феврале!')
            elif month != 2 and day > day_dict.get(month):
                print('Некорректное число!')
            else:
                print('Дата корректна!')


Date.validation('29-02-2016')

print(Date.cast('29-02-2016'))

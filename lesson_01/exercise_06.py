# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#

current = float(input("Введите текущий результат, км: "))
purpose = float(input("Введите результат, которого требуется достичь, км: "))
day = 1

while current <= purpose:
    current *= 1.1
    day += 1

print("На {}-й день спортсмен достиг результата - не менее {} км.".format(day, purpose))
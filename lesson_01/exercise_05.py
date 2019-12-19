# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Введите показатель выручки за период, руб: "))
costs = float(input("Введите показатель издержек за период, руб: "))
profit = proceeds - costs

if profit > 0:
    rate = "{:.2f}".format((profit / proceeds) * 100)
    print("Компания работает с прибылью! Рентабельность выручки составляет {}%.".format(rate))
    num_empl = int(input("Введите количество сотрудников, работающих в компании: "))
    relative = "{:.2f}".format(profit / num_empl)
    print("Прибыль в расчете на одного сотрудника составляет {} руб".format(relative))
elif profit == 0:
    print("Выручка равняется издержкам. Компания работает без прибыли.")
else:
    print("Компания терпит убытки!")

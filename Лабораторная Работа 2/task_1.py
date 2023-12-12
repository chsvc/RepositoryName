money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = money_capital + salary
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while budget >= spend:
    month += 1  # прожили месяц
    budget -= spend  # потратили
    grow_spend = spend * increase  # насколько выросли цены
    budget += salary  # пришла зп
    spend += grow_spend  # выросли траты

print("Количество месяцев, которое можно протянуть без долгов:", month)

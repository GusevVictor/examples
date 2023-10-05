print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

# Решение
count_of_month = 12
middle_salary = 0
sum_salary = 0

print(f'Укажите зарплату за каждый месяц из {count_of_month} месяца(ев)')

for salary in range(0, count_of_month):
  salary_per_month = int(input('Укажите зарплату сотрудника за месяц: '))
  sum_salary += salary_per_month

middle_salary = (sum_salary / count_of_month)
print(f'Средняя заработная плата за месяц составляет: {int(middle_salary)}')

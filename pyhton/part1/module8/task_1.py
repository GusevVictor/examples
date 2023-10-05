print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.

# Решение
total_buckwheat = 100
total_month = 0

for month in range(total_buckwheat - 4, -1, -4):
  total_month += 1
  print(
    f'Через {total_month} месяцa(ев) останется {month} килограмм(а) гречки!')
else:
  print(f'Гречки больше не осталось..! Вы продержались {total_month} месяцев!')
print('Конец работы программы!')

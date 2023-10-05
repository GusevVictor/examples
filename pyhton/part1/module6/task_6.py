print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

# Решение
start_deposit = int(input('Вклад в банке составляет (рублей): '))
percent_per_year = int(input('Ежегодно он увеличивается на (процентов): '))
end_deposit = int(input('Желаемая сумма (рублей): '))
current_deposit = start_deposit
years = 0

while end_deposit > current_deposit:
  current_deposit = ((current_deposit) * (1 + percent_per_year / 100))
  current_deposit = int(current_deposit)
  years += 1
print('Прежде чем сумма достигнет значения', end_deposit, ', пройдет не менее', years, 'лет')

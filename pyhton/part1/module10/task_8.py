print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

# Решение

pit_depth = int(input('Укажите глубину ямы: '))
pit_weight = (pit_depth * 2)
center = (round(pit_weight / 2) - 1) + 1

for row in range(pit_depth):
  for column in range(pit_weight):
    if column in range(0 + row + 1, pit_weight - row - 1):
      print('.', end='')
    else:
      if column < center:
        print(center - column, end='')
      else:
        print((column - center) + 1, end='')
  print()

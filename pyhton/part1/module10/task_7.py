print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

# Решение
pyramid_height = int(input('Укажите количество уровней пирамидки: '))
pyramid_weight = (pyramid_height * 3) + 2
center = (round(pyramid_weight / 2) - 1)
count, number = 0, 1

if pyramid_height % 2 != 0:
  center += 1
else:
  pyramid_weight -= 1

for row in range(pyramid_height):
  for column in range(pyramid_weight):
    if column in range(center - count, (center + 1) + count, 4):
      print(number, end='')
      number += 2
    else:
      print(' ', end='')
  count += 2
  print()

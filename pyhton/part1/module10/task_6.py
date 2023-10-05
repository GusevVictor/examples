print('Задача 6. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

# Решение

pyramid_height = int(input('Укажите высоту пирамидки: '))
pyramid_weight = (pyramid_height * 2) - 1
center = (round(pyramid_weight / 2) - 1)
if pyramid_height % 2 != 0:
  center += 1

for row in range(pyramid_height):
  for column in range(pyramid_weight):
    if column in range(center - row, (center + 1) + row):
      print('#', end='')
    else:
      print(' ', end='')
  print()

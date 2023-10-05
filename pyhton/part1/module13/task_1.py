print('Задача 1. Урок информатики 2')

# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введитечисло: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3


# Решение
def calculate_number_more_than_one(number):
  count = 0
  while number > 10:
    number /= 10
    count += 1
  print('Формат плавающей точки: х =', number, '* 10 **', count)


def calculate_number_lower_than_one(number):
  count = 0
  while float(number) < 1:
    number *= 10
    count -= 1
  print('Формат плавающей точки: х =', round(number, 1), '* 10 **', count)


number_for_convert = float(input('Введите число (больше нуля): '))

if number_for_convert > 1:
  calculate_number_more_than_one(number_for_convert)
elif number_for_convert > 0:
  calculate_number_lower_than_one(number_for_convert)
else:
  print('Ошибка ввода! Число должно быть больше нуля!')

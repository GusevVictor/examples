print('Задача 8. Кинотеатр. Вариант решения №1. Только цикл for')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

# Решение
boys_count = int(input('Введите кол-во мальчиков: '))
girls_count = int(input('Введите кол-во девочек: '))
limit_max = boys_count
limit_min = girls_count
answer = ''
gender_add = 'B'
genders = 'BG'
permit = True

if girls_count > boys_count:
  gender_add = 'G'
  genders = 'GB'
  limit_max, limit_min = limit_min, limit_max

if (limit_max - limit_min) > limit_min:
  permit = False
  answer = 'Нет решения'

if permit:
  for i in range(limit_max - limit_min):
    answer += genders + gender_add
  for i in range(limit_min - (limit_max - limit_min)):
    answer += genders

print(answer)

############## Конец варианта №1 ##############

print('Задача 8. Кинотеатр. Вариант решения №2. Циклы for и while')

boys_count = int(input('Введите кол-во мальчиков: '))
girls_count = int(input('Введите кол-во девочек: '))
limit_max = boys_count
limit_min = girls_count
answer = ''
gender_add = 'B'
genders = 'BG'
permit = True

if girls_count > boys_count:
  gender_add = 'G'
  genders = 'GB'
  limit_max, limit_min = limit_min, limit_max

if (limit_max - limit_min) > limit_min:
  permit = False
  answer = 'Нет решения'

if permit:

  for i in range(1, limit_min + 1):
    answer += genders

  if limit_max != limit_min:
    difference = limit_max - limit_min
    j = 3
    while difference > 0:
      answer = answer[:j] + gender_add + answer[j:]
      difference -= 1
      j += 3

print(answer)

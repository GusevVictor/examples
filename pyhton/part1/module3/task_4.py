print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

# Решение
a = int(
  input('Введите длину катета (в см.) "a" прямоугольного треугольника: '))
b = int(
  input('Введите длину катета (в см.) "b" прямоугольного треугольника: '))

# Расчет
s = (a * b) / 2

# Ответ
print('Площадь прямоугольного треугольника =', s, 'см2')

print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

# Решение
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a <= b:
  pass
else:
  b = a
if b <= c:
  pass
else:
  c = b
print('Максимальное из этих трёх чисел:', c)

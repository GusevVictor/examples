print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Решение

number = int(input('Введите число: '))
for i in range(1, number + 1):
  for j in range(i):
    print(f'{i}', end=' ')
  print()

# Можно всё сделать двумя строками кода, но условия домашней работы требуют использования вложенных циклов:
# for i in range(1, number + 1):
#   print((str(i)+' ') * i)

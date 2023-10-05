print('Задача 1. Сумма чисел')

# Напишите функцию calculate_summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


# Решение
def calculate_summa_of_number(number_for_calculate):
  summa_of_number = 0
  for number_i in range(1, number_for_calculate + 1):
    summa_of_number += number_i
  return summa_of_number


number = abs(int(input('Введите целое, положительное число: ')))
result = calculate_summa_of_number(number)

print(f'Я знаю, что сумма чисел от 1 до {number} равна {result}')

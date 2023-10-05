print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

# Решение
number = 1
sum = 0
while number != 0:
  print(
    '\nВведите натуральное число.\nУкажите число ноль, когда ввод будет закончен: ',
    end='')
  number = int(input())
  digit_sum = 0
  for digit in str(number):
    digit_sum += int(digit)
  else:
    if digit_sum > sum:
      number_max = number
      sum = digit_sum
else:
  print(
    f'\n---\nНатуральное число {number_max}, дало наибольшее по сумме цифр: {sum}.'
  )

print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


# Решение
def main_menu():
  print('Добро пожаловать!')
  number = int(input('Введите число: '))
  print(
    '\nВывести сумму его цифр (1), максимальную (2) или минимальную цифру (3).'
  )
  action = int(input('Введите действие (1-3): '))
  if action == 1:
    result = calculate_summa_of_digit(number)
    print(f'Сумма цифр числа: {result}\n')
  elif action == 2:
    result = get_maximum_digit(number)
    print(f'Максимальная цифра числа: {result}\n')
  elif action == 3:
    result = get_minimum_digit(number)
    print(f'Минимальная цифра числа: {result}\n')
  else:
    print(f'Действие нужно выбирать в диапазоне 1-3.\n'
          f'Вы выбрали: {action}. Попробуйте снова!\n')


def calculate_summa_of_digit(number_for_calculate):
  summa_of_digit = 0
  for digit in str(number_for_calculate):
    summa_of_digit += int(digit)
  return summa_of_digit


def get_maximum_digit(number_for_get_maximum_digit):
  maximum_digit = 0
  for digit in str(number_for_get_maximum_digit):
    digit = int(digit)
    if maximum_digit < digit:
      maximum_digit = digit
  return maximum_digit


def get_minimum_digit(number_for_get_minimum_digit):
  minimum_digit = number_for_get_minimum_digit
  for digit in str(number_for_get_minimum_digit):
    digit = int(digit)
    if minimum_digit > digit:
      minimum_digit = digit
  return minimum_digit


while True:
  main_menu()

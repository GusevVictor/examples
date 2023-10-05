print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


# Решение
def main_menu():
  get_numbers()


def get_numbers():
  number_1 = int(input('Введите первое число: '))
  number_2 = int(input('Введите второе число: '))
  print()
  get_reverse_digit_in_two_numbers(number_1, number_2)


def get_reverse_digit_in_two_numbers(first_number, second_number):
  first_number_reversed = int(str(first_number)[::-1])
  second_number_reversed = int(str(second_number)[::-1])
  print(f'Первое число наоборот: {first_number_reversed}\n'
        f'Второе число наоборот: {second_number_reversed}\n')
  calculate_sum_of_two_numbers(first_number_reversed, second_number_reversed)


def calculate_sum_of_two_numbers(number_a, number_b):
  sum_of_two_numbers = number_a + number_b
  print(f'Сумма: {sum_of_two_numbers}')
  get_reverse_digit_in_one_number(sum_of_two_numbers)


def get_reverse_digit_in_one_number(number):
  number_reversed = int(str(number)[::-1])
  print_result(number_reversed)


def print_result(result):
  print(f'Сумма наоборот: {result}')


main_menu()

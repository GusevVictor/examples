print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.


# Решение
def main_menu():
  print('Добро пожаловать!')
  get_numbers()


def get_numbers():
  number_1, number_2, number_3 = input(
    'Укажите три числа (через пробел): ').split()
  calculate_maximum_of_three_numbers(int(number_1), int(number_2),
                                     int(number_3))


def calculate_maximum_of_three_numbers(number_a, number_b, number_c):
  max_number = calculate_maximum_of_two_numbers(number_a, number_b)
  max_number = calculate_maximum_of_two_numbers(max_number, number_c)
  print_result(max_number)


def calculate_maximum_of_two_numbers(first_number, second_number):
  if first_number > second_number:
    return first_number
  return second_number


def print_result(result):
  print(f'Наибольшее число из трех: {result}')


main_menu()

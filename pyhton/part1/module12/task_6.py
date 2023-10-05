print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел


# Решение
def calc_gcd(number_a_for_calc_gcd, number_b_for_calc_gcd):
  if (number_a_for_calc_gcd == 0) or (number_b_for_calc_gcd == 0):
    gdc_of_numbers = 0
  else:
    if number_a_for_calc_gcd > number_b_for_calc_gcd:
      maximum_number = number_b_for_calc_gcd
    else:
      maximum_number = number_a_for_calc_gcd
    for number_i in range(1, maximum_number + 1):
      if ((number_a_for_calc_gcd % number_i == 0)
          and (number_b_for_calc_gcd % number_i == 0)):
        gdc_of_numbers = number_i
  return gdc_of_numbers


number_a = abs(int(input("Введите первое число: ")))
number_b = abs(int(input("Введите второе число: ")))

result = calc_gcd(number_a, number_b)

print(f'НОД числа {number_a} и числа {number_b}, равен: {result}')

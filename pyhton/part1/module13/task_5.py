print('Задача 5. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний


# Решение
def main():
  start_pendulum_amplitude = int(input('Введите начальную амплитуду (см): '))
  stop_pendulum_amplitude = float(input('Введите амплитуду остановки (см): '))
  result = calculate_count_of_pendulum_swing(start_pendulum_amplitude,
                                             stop_pendulum_amplitude)
  print(f'\nМаятник считается остановившимся через {result} колебаний')


def calculate_count_of_pendulum_swing(start_pendulum, stop_pendulum):
  current_amplitude = start_pendulum
  count = 0
  while current_amplitude > stop_pendulum:
    count += 1
    current_amplitude = current_amplitude - (current_amplitude / 100 * 8.4)
  return count


main()

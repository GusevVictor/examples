print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

# Решение
x_horse, y_horse, x_point, y_point = 1, 1, 1, 1

# Обеспечение контроля ввода (согласно условиям)
print('Введите местоположение коня (0 - 0.8):')
while (x_horse < 0) or (x_horse > 0.8):
  x_horse = float(input('X: '))
while (y_horse < 0) or (y_horse > 0.8):
  y_horse = float(input('Y: '))

print('Введите местоположение точки на доске:')
while (x_point < 0) or (x_point > 0.8):
  x_point = float(input('X_point: '))
while (y_point < 0) or (y_point > 0.8):
  y_point = float(input('Y_point: '))

# Вычисление
x_horse, y_horse = int(x_horse * 10), int(y_horse * 10)
x_point, y_point = int(x_point * 10), int(y_point * 10)

print(
  f'Конь в клетке ({x_horse}, {y_horse}). Точка в клетке ({x_point}, {y_point}).'
)

delta_x = abs(x_horse - x_point)
delta_y = abs(y_horse - y_point)

if delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1:
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')

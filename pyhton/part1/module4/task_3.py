print('Задача 3. Следим за расписанием')

# После выполненной задачи Вася устал и понял, что весь следующий день ему придётся восстанавливать силы. Вася решил, что работать он будет только в чётные дни и написал небольшую программу, которая поможет ему не пропустить рабочий день.

# Напишите программу, которая проверяет, чётное ли число ввёл пользователь, и выводит соответствующее сообщение.

# Подсказка: для проверки чётности используйте оператор %.

# Решение

day_of_the_month = int(input('Введите день месяца: '))

day_of_the_month %= 2

if day_of_the_month != 1:
  print('Пора за работу!')
else:
  print('Сегодня не рабочий день!')

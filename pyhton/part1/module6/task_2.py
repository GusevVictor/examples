print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

# Решение
debtor_name = input('Имя должника: ')
debt_amount = int(input('Сумма долга: '))
deposited_amount = 0

print(
      debtor_name+', ваша задолженность составляет', debt_amount, 'рублей.')

while True:
  deposited_amount = int(input(
    'Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  print()
  if deposited_amount >= debt_amount:
    print('Отлично', debtor_name+'! Вы погасили долг. Спасибо!')
    break
  print('Маловато,', debtor_name+'. Давайте ещё раз.')
  
print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1


# Решение
def calculate_count_letters(text_for_count_letters, digit_for_count_letters,
                            letter_for_count_letters):
  count_digit, count_letter = 0, 0
  for symbol in text_for_count_letters:
    if digit_for_count_letters == symbol:
      count_digit += 1
    elif letter_for_count_letters == symbol:
      count_letter += 1
  return count_digit, count_letter


text = input('Введите текст: ').lower()
digit = str(int(input('Какую цифру ищем? ')))
letter = input('Какую букву ищём? ').lower()

result = calculate_count_letters(text, digit, letter)
print('\n'
      f'Количество цифр {digit}: {result[0]}\n'
      f'Количество букв {letter}: {result[1]}\n')

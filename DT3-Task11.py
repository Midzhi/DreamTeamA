# Задание 11:
# Попросить пользователя ввести слова через пробел.
# Отсортировать слова по количеству символов и вывести на экран результат.

# Пример input: сон машина стол книга девочка
# Результат: сон стол книга машина девочка

text = input('Введите текст: ')

t = text.split()
new_text = ''
for i in sorted(t, key=lambda a:len(a)):
    new_text = new_text + ' ' + i

print(new_text)

# Задание 10:
#     Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(),
#     чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
#     Подсказка: необходимо заменить \n на пробел.

#     То есть, это нужно проделать еще до фильтрации.
#     Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.

import re

with open('text.txt', 'r') as f:
    text = f.read()
new_text = re.split('\.|\,|\n|\ ', text)

def func_p(word):
    if 'p' in word:
        return True


filter_text = filter(func_p, new_text)
print(list(filter_text))
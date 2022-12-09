# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python.
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
import re

def list_c():
    list_c = []
    with open('text.txt', 'r') as f:
        text = f.read()
        for string in re.split('\.|\,|\n| ', text):
            if string.startswith('c') or string.startswith('C'):
                list_c.append(string)
    print(list_c)

list_c()
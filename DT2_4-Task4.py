# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().

def float_func():
    a = float(input('Введите число: '))
    max_num = a
    min_num = a
    for i in range(5):
        num = float(input('Введите число: '))
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print('Максимальное число:', round(max_num, 2))
    print('Минимальное число:', round(min_num, 2))

float_func()
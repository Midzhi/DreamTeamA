# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа.
#     Требуется положительные поместить в один список, а отрицательные - в другой.

def func(my_list):
    positive_list = []
    negative_list = []
    for i in my_list:
        if i > 0:
            positive_list.append(i)
        elif i < 0:
            negative_list.append(i)
    print('Список положительных цифр:', positive_list)
    print('Список отрицательных цифр:', negative_list)

my_list = [-1, 0, 2, 3, -4, 5, -6, -4, 2, 1, 2]

func(my_list)
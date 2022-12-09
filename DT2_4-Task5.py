# Задание 5:
        # Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое

def number():
    number = int(input('Введите число: '))
    max_num = 0
    min_num = 9
    while number > 0:
        num = number % 10
        number //= 10
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print('Максимальное число:', max_num)
    print('Минимальное число:', min_num)

number()

# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(arg):
    if 3 <= arg <= 5:
        return 'Весна'
    elif 6 <= arg <= 8:
        return 'Лето'
    elif 9 <= arg <= 11:
        return 'Осень'
    else:
        return 'Зима'

print(season(5))
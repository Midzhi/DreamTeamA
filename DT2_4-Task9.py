# Задание 9:
#     Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
#         и возвращает функцию, которая также берет два аргумента (числа),
#             и возвращает результат умножения аргументов внешней функции плюс результат деления
#                 аргументов внутренней функции.
#     Подсказка: (outer_arg1 * outer_arg1) + (outer_arg1 / outer_arg1)

def multi(outer_arg1, outer_arg2):
    multi = outer_arg1 * outer_arg2
    def div(outer_arg1, outer_arg2):
        div = outer_arg1 / outer_arg2
        return multi + div

    return div(outer_arg1, outer_arg2)

print(multi(6,2))
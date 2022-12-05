# Задание 3:
# Вам даны 2 листа:

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']

# Напишите функцию которая их принимает и сравнивает на равность.
# Пример где листы равны:

    # a + bc + de = abcde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['1', '23', 'abcde']

# Пример где листы НЕ равны:

    # a + cb + de = acbde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['123', 'de', 'abc']

def list_equale(list_1, list_2):
    sum_list_1 = ''
    sum1 = sum_list_1.join(list_1)

    sum_list_2 = ''
    sum2 = sum_list_2.join(list_2)

    if sum1 == sum2:
        return 'Эти списки равны'
    else:
        return 'Эти списки не равны'

list1 = ['a', 'bc', 'de']
list2 = ['ab', 'c', 'de']

print(list_equale(list1, list2))
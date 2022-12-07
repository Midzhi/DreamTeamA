
# Вам даны 2 листа:

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']

# Напишите функцию которая их принимает и сравнивает на равность.
# Пример где листы равны:

    # a + bc + de = abcde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['1', '23', 'abcde']

def list_equil ( list_1,list_2):
    sum_list1 = ''
    sum1 = sum_list1.join(list_1)

    sum_list2 = ''
    sum2 = sum_list2.join(list_2)
    if sum1 == sum2:
        return 'Списки равны'
    else:
        return 'Списки не равны'

l1 = ['a', 'bc', 'de']
l2 = ['ab','c', 'de']
print(list_equil(l1, l2))

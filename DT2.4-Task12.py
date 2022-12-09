
# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа. 
#     Требуется положительные поместить в один список, а отрицательные - в другой.
##################

def posneg(arg):
    positive = []
    negotive = []
    for i in arg:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negotive.append(i)
    return positive,negotive

num = [2,4,-5,6,-7,65,-45,85,-105,104]
pos,neg = posneg(num)
print(pos)
print(neg)
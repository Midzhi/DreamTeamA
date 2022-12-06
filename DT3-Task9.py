# Задание 9:
# Попросить пользователя ввести текст.В результате
# вывести процент букв в верхнем регистре(заглавные)
# и в нижнем регистре(прописные)

text = input('Введите текст: ')
count_up = 0
count_low = 0
for i in list(text):
    string = ''.join(i)
    if string.isupper():
        count_up += 1
    elif string.islower():
        count_low += 1
symbol_sum = count_up + count_low
print(f'В данном тексте {count_up} заглавных букв: {round((count_up/symbol_sum * 100), 2)}%')
print(f'В данном тексте {count_low} строчных букв: {round((count_low/symbol_sum * 100), 2)}%')

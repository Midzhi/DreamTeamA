
# Задание 10:
#     Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(), 
#     чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”),
#  что содержат букву ‘p’.
#     Подсказка: необходимо заменить \n на пробел. 

#     То есть, это нужно проделать еще до фильтрации. 
#     Функция, которая будет передана в filter() должна возвращать True, если в слове 
# есть буква ‘p’.
#####################################################################


text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
# start = -1
# count = 0

# while True:
#     start = text.find('p', start+1)
#     if start == -1:
#         break
#     count += 1
# print('in text ', count ,'letters')

# print(type(text))

# print(f'List of Words = {text.split()}')

def filter_check(text_to_check):

    text_to_check = 'p'
    for i in text_to_check:
        if i in text:
            return True
        else:
            return False



print('in there', text)

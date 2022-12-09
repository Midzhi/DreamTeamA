
# pairs = {}

# В Tuple перечислены элементы, где идёт строгая очерёдность STRING и INTEGER.
# То есть если перед вами элемент типа данных STRING то следующий точно INTEGER и наоборот.
# keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 'six', 7, 'seven', 
# 'eight', 8, 'nine',9, 10, 'ten', 11, '11', 12 ,'13')
# Проходя по TUPLE необходимо брать элементы по парно, один элемент может относиться только
# 
#  и только к одной паре.
# Ваша задача выявить если элемент является типом данных string() то записывать его как
#  ключ в Dictionary -> pairs.



keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 ,'six', 7, 'seven', 
'eight', 8, 'nine',9, 10, 'ten', 11, 'eleven', 12 ,'twelve')

k_l = []
v_l = []

for i in keys_values:
    if type(i) == str:
        k_l.append(i)
    else:
        v_l.append(i)

print(k_l)
print(v_l)

pairs = dict()

for i in range(len(k_l)):
    pairs[k_l[i]] = v_l[i]

print(pairs)


    



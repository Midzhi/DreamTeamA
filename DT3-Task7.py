

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


    



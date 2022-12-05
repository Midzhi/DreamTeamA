pairs = {}



keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 ,'six', 7, 'seven', 
 'eight', 8, 'nine',9, 10, 'ten', 11, '11', 12 ,'13')



k = [int(s) for s in str.sorted(keys_values) if s.isdigit()]
print(k)











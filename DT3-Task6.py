# Задание 6:
# В Python есть такой тип Данных как Boolean...
# Создайте TUPLE который ТЕХНИЧЕСКИ состоит из 4 Булевых ЗНАЧЕНИЙ.

################################################################################

tuple1 = (10,5,3)
tuple2 = (5,20,10)
tuple3 = (5,10,8)
tuple4 = (10,20,5)

if tuple1 <= tuple2 <= tuple3 and tuple2 >= tuple4:
    print('False')

elif tuple1 >= tuple2 >= tuple3 and tuple2 <= tuple4:
    print('True')
else:
    print('nothing')


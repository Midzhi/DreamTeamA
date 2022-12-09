import random as rd

number = input('enter any number: ')

random_number = rd.randint(0,10)

for i in number:

    if i == random_number:

        print('good job')

else:
    print('false')
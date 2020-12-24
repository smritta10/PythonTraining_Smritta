# Exercise 9

import random
random_number = random.randint(1,101)
answer = ''
while answer!= 'no':
    number = int(input("Enter your guess between 1-100: "))
    if number == random_number:
        print('You won')
        break
    else:
        print('Do you want to continue:')
        answer = input()
        continue

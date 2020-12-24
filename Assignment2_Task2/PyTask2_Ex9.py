# Exercise 9

import random
random_number = random.randint(1,100)
win = False
while win!= True:
    num = int(input('Enter your guess: '))
    if num == random_number:
        win= True
        print('You won')
        break
    else:
        print("Try again")
        continue


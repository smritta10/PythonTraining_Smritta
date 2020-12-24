# Exercise 11

import random
random_number = random.randint(1,101)
counter = 1
while counter <=5:
    print("Type in the ", counter, "number")
    number = int(input())
    counter += 1
    if number == random_number:
        print('Good guess')
        break
    elif (counter== 6):
        print("Sorry but that was not very successful")  
        break  
    else:
        print('Try Again!')
        continue

# Exercise 8

str = input("Enter a String: ")

count_letters, count_digits = 0, 0
for i in str:
    count_letters += i.isalpha()
    count_digits += i.isnumeric()

print('Input string is: ', str) 
print("Count of letters: ", count_letters)
print("Count of digits: ", count_digits)


# Exercise 1
firstname, age, female= 'Smritta', 29, True
print(firstname, age, female)

# Exercise 2
x= complex(1,2)
print(x)
y= 10
print(y)
print(type(y))

x, y = y, x
print(x)
print(y)

#Exercise 3
#Swap using a 3rd var
num1= 15
num2= 18
Print('Numbers before swap: '. num1, num2)

temp= num1
num1= num2
num2= temp
print('Numbers after swap: ', num1, num2)

#swap without using a 3rd var
num1= 15
num2= 18
print('Actual Numbers : ', num1, num2)
num1, num2 = num2, num1
print('Numbers after swap:', num1, num2)

#Exercise 4
test_input= str(input('Enter your name'))
# print in Python3.x
print(test_input)
#print in Python2.x
print test_input

#Excercise 5
input1= int(input('Enter first number between 1-10: '))
input2= int(input('Enter second number between 1-10: '))
z= input1 + input2
result= z +30
print('Final Output is: ', result)

#Exercise-6  
var= input('Enter any type of variable: ')
print(type(var))

#Exercise-7
#Upper Camel case
MyNameIs = 'Smritta'
#Lowe Camel case
myAgeIs= 29
#Snake case
i_live_in = "San Francisco"

#Exercise-8
a= 'Smritta'
print('Value of a :' , a, ',', 'Id of a is: ',  id(a))
 #assigning another value to a
a= 29
print('New Value of a :' , a,',','New Id of a is: ',  id(a))
# Yes the value of 'a' will be overwritten because previously
# 'a' was pointing to a different memory location where 'Smritta'
# was saved as a variable. But when we replaced the value with 29
# it started pointing to a different memory location, so id changed.


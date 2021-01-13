Task-4

#Ex-1 
str= input('Enter a string: ')
rev = str[::-1]
print('Reverse of string is: ', rev)

---------------------------------------------------
#Ex-2
str= input('Enter a word: ')
upper_count= 0
lower_count=0

for i in str:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1
print('Number of Upper case characters is: ', upper_count)
print('Number of Lower case characters is: ', lower_count)

-------------------------------------------------------------
#Ex-3
def unique():
    l1= input('Enter your list:').split(',')
    s1= set(l1) #converting list into Set to get unique values
    unique_list= list(s1)
    print(unique_list)
unique()

------------------------------------------------------

#Ex-4
items= []
for i in input().split('-'):
    items.append(i)
items.sort()
print('-'.join(items))

---------------------------------------------------

#Ex-5
x= input('Enter your sentence: ')
x.upper()
----------------------------------------------------

#Ex-6
def sum1(x1, x2):
    answer= int(x1) + int(x2)
    print("Sum is:", answer)
        
x1= input('Enter the first num:')
x2= input('Enter the second num:')

sum1(x1, x2)

------------------------------------------------------


#Ex-7
def maxlen(): 
    str1= input('Enter first string:')
    str2= input('Enter second string:')
    l1= len(str1)
    l2= len(str2)
    print('Length of first string: ', l1)
    print('Length of second string: ', l2)
        
    if l1 > l2:
        print('Str1 has max length:', str1)
    elif l2 < l1:
        print('Str2 has max length:', str2)
    else:        
        print('Both strings have equal length:')
        print(str1)
        print(str2)
        
maxlen()

-----------------------------------------------------

# Ex-8 
def square1():
    list1= []
    t= ()
    for i in range(1,21):
        list1.append(i*i)
    print('Actual list having square:', list1)
    t= tuple(i for i in list1)
    return t 
square1()

---------------------------------------------------
#Ex-9
def showNumbers(limit):
    for i in range(0, limit+1):
        print(i, end='')
        if i%2==0:
            print(' EVEN')
        else:
            print(' ODD')
showNumbers(int(input('Enter a limit:')))
            
----------------------------------------------------

#Ex-10
even= list(filter(lambda x: x%2==0, range(1,21)))
print(even)

----------------------------------------------------
#Ex-11
var1= list(filter(lambda x:x%2==0, [1,2,3,4,5,6,7,8,9,10])) # to filter the even numbers
var2= list(map(lambda x: x**2, var1)) # to calculate the square of even numbers
print('List of Even nums:', var1)
print('Square of Even nums:', var2)

---------------------------------------------------
# Ex-12
def compute():
    try:
        var= 5/0
    except:
        print("5/0 is undefined")
compute()

-------------------------------------------------------

# Ex-13
# Flatten a list using reduce()

from functools import reduce

r = reduce(lambda x,y : str(x)+str(y),[1,2,3,4,5,6,7])
print(r)
--------------------------------------------------------

# Ex- 14
num= int(input('Enter a number: '))
div= list((filter(lambda x: x%3!=0 and x%7==0, range(0,num+1))))
print(div)

---------------------------------------------------------

#Ex-15
result1= (lambda x:x*x,[10,20,30])

result2= list(map(lambda x:x, result1))
print(result2)

---------------------------------------------------
#Ex- 16

i) def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

Output- 2
because it will first return 1 then finally block will get executed and overrite 1 with 2. 
----------------------------------------------------------

ii) def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

Output-> will be
after f
after f?
But will also throw error for function f(x,4) which doesn't exist













			








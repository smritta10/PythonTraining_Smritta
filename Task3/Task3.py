
#Question 1
diff_list= [10,'Smritta', 10.5,'1+2j', 20,'Singh', 113.0, '3+4j', 100, 'Python_learning']
print(diff_list)

-----------------------------------------------------
#Question 2
list1= [10,20,30,40,50]
s1= list1[ :5]  #actual list
s2= list1[ : :-1]  # lists items in reverse order
s3= list1[1:5:2] # lists item from 0 to 4 skipping 2nd item
print('Different slicing results: ', s1, ',', s2, ',', s3)

--------------------------------------------------
# Question 3
L1= [2,4,6,8]
total= sum(L1) # find the sum
print('Sum of all items in list is: ', total)

result= 1
for i in L1:
    result= result *i
print('Multiplication output is:', result)

-------------------------------------------------------
#Question 4
myList= [2,4,6,8,10]
print('Max number from the list is:', max(myList))
print('Min number from the list is:', min(myList))

-----------------------------------------------------
#Question 5
x= filter(lambda x: x%2==0,[5,10,15,20,25,30])
print(list(x))

-------------------------------------------------
#Ex-6
l= list()
for i in range(1,31):
    l.append(i**2)
print('First 5 elements square is: ', l[:5])
print('Last 5 elements square is: ', l[-5:])

-------------------------------------------------
#Ex-7
list1= [2,4,6,8,10]
list2= [1,3,5]
list1.pop()
print('List after removing last item:', list1)
list1.extend(list2)
print('Final list after adding a list:', list1)

-------------------------------------------------
#Ex-8
d= {} # empty dictionary
dict1= {1:10, 2:20}
dict2= {3:30, 4:40}
d.update(dict1)
d.update(dict2)
print('Concatenated dictonary is:', d)

-------------------------------------------------
#Ex-9
num= int(input('Input a number:'))
dict= {}
for i in range(1,num+1):
    dict[i]= i*i
    
print('My dictionary is:', dict)

--------------------------------------------------
#Ex-10

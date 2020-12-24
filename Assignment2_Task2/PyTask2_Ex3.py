#Exercise 3

a, b, c= 10, 20,30
avg = (a+ b+c)/3
print("avg =", avg)

if(avg >a and avg>b and avg>c):
    print("Avg is higher than ", a, ',', b, ',', c)
elif (avg> a and avg> b):
    print('Avg is higher ', a, ',', b, ',', c)
elif(avg> a and avg> c):
    print("Avg is higher than ", a, ',', c) 
elif(avg>b and avg>c):
    print("Avg is higher than ", b, ',', c)
elif(avg> a):
    print("Avg is higher than ", a,) 
elif(avg>b):
    print("Avg is higher than ", b)
else:
    print('Avg is just higher than ', c)
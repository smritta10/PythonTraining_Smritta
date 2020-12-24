#Exercise 5

all_val= []
for i in range(2000, 3201):
    if(i%7 == 0 and i% 5!=0):
        all_val.append(i)
        print(all_val)
            
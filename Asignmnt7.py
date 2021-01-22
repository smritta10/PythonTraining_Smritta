
TASK 7

# Ex-1

from math import sqrt

C=50
H=30

varD= input('Enter D values: ').split(',')
print(varD)

l= []
for i in varD:
    res= sqrt((2*C*int(i))/H)
    l.append(res)
print('Square root is: ', l)

----------------------------------
# Ex-2

class Shape:
    
    def area():
        ar= 0
        
class Square(Shape):
    def __init__(self, length):
        self.length= length
        
                    
    def area(self):
        print(self.length)
        ar= self.length**2
        return ar

ob1= Square(10)
print(ob1.area())

-------------------------------------------

# Ex-5






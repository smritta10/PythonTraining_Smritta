
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

------------------------------------------
# EX-4  (need to do this again with more clarity)

class Time:
    def __init__(self, hours,minutes):
        self.hours= hours
        self.minutes= minutes
        
    def addTime(obj1, obj2):
        hours= obj1.hours+ obj2.hours
        min1= obj1.minutes+ obj2.minutes
    
    def displayTime():
        print(str(hours)+ ' hour and' + str(min1) +' minutes')
              
    def displayMinute():
        print(hours*60 + min1)
        
obj1= Time(1,32)
obj2= Time(2,50)
addTime(obj1, obj2)
displayTime()





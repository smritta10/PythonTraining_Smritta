
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function divides two numbers
def divide(x, y):
    return x / y
	
# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function gives Average of two numbers
def average(x, y):
    return (x + y)/2


print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Average")

while True:
    # Take input from the user
    var = input("Enter your choice: ")

    # Check if var is one of the options
    if var in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if var == '1':
            print('Sum of', num1, 'and',  num2, 'is: ', add(num1, num2))

        elif var == '2':
            print('Substraction of', num1, 'and',  num2, 'is: ', subtract(num1, num2))

        elif var == '3':
            print('Division of', num1, 'and',  num2, 'is: ', divide(num1, num2))
			
        elif var == '4':
            print('Multiplication of', num1, 'and',  num2, 'is: ', multiply(num1, num2))	

        #elif var == '5':
            #first= int(input('Enter first number: '))
            #second= int(input ('Enter second number: '))
            #print('Average of ', first, 'and', second, 'is: ', average(first, second))
        break
    elif var == '5':
        first= int(input('Enter first number: '))
        second= int(input ('Enter second number: '))
        print('Average of ', first, 'and', second, 'is: ', average(first, second))
    else:
        print("Invalid Input")
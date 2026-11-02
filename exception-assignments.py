
#! Assixception-handling practice Safe integer input
#Ask the user for an integer. Use try and except to print 'Valid integer' or 'Invalid integer'. Handle ValueError.

# try:
#     user_input = int(input("Enter a number: "))

# except ValueError:
#     print("Invalid integer") 

# else:
#     print("Valid integer")

#! 2. Division calculator
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print('Enter valid number')
except ZeroDivisionError:
    print('Cannot divide by zero')

else:
    print("Result:", result)

finally:
    print("Program execution completed")


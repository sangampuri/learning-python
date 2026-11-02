
#! Example 1
# try:
#     first_input = int(input("Enterfirst number "))
#     second_input = int(input("Enterfirst number "))

#     result = first_input / second_input
#     print(f"Result: {result}")

# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# except ValueError:
#       print("Please enter valid integers.")

#! Example 2
# try:
#   available_balance = 100000
#   amount =   int(input("Enter widthdrawl amount: "))
#   remaining_balance = available_balance - amount

# except ValueError:
#   print("Please enter valid amount")

# else:
#   print("Widthdrawl amount:", amount)
#   print("Available balance:", remaining_balance)

#! Example 3

# try:
#     num = int(input("Enter a number: "))

# except ValueError:
#     print("Please enter a valid number")

# else:
#     print(f"The number is {num}")
#     print("It's square is ",num**2)

#! Example 4
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


finally:
    print("Calculation attempt finished.")
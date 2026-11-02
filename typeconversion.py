# Getting input from users
#value = input('Enter your name: ')
#print(value)

# Calculating tax rate using type conversion int()
price = input('Enter the price($): ')
tax = input('Enter tax(%): ')
tax_amt = int(price)*int(tax)/100
print(f"The taxt amount is $:{tax_amt}")

# Getting the type of a value

amount = type(100)
print(amount)
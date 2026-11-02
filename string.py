help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)


#Using variables in Python strings with the f-strings 
name = 'John'
mesage = f'Namaste {name}'

print(mesage)


#Concatenating Python strings
greeting = 'Good ' 'Morning!'
print(greeting)

#Accessing string elements 
str = "Python String"
print(str[0]) # P
print(str[1]) # y
print(str[6]) # 

#Use negative indexing to get character form last
str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

# Getting the length of a string 
str = "Python String"
str_len = len(str)
print(str_len)

#Slicing strings 
str = "Python String"
print(str[0:2]) # [start:end]
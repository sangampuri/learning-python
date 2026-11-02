
#! 1. Search a list
numbers = [10, 20, 30, 40]
for n in numbers:
    if n == 30:
        print("Found")
        break

else:
    print('Not found')

#! 2. Find a name
names = ['Ram', 'Hari', 'Gita']
for n in names:
    if n == 'Sita':
        print('Name found')
        break

else:
    print('Name not found')

#! 3. Countdown

n=5
while n >= 1:
    print(n)
    print('Blast off')
    n -=1
else:
    print('loop finished')

#!4. Stop early
# Loop through range(1, 10). Print each number and break when the number equals 4. Add an else block. Predict which lines will appear.

for x in range(1,10):
    if x != 4:
        print(x)
    if x==4:
        break
else:
    print('idk what is the use of else here')

#! 5. Prime number checker
numbers = [1,2,3,5,7,11,13,15,16,]
for n in numbers:
    if n % 


# Creating a function that counts form 3 to 1 recursively

def count(num): #5
    print(num)
    next = num - 1
    
    if(next > 0):
        count(next)
    else:
        print('Counting completed')




count(3)
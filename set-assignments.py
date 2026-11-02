
#! 1. count unique names
names = {'Ram','Sita', 'Ram', 'Hari', 'Sita', 'Gita'} 
#print(len(names)) 

#! 2. Add and remove
fruits = {'apple', 'banana', 'mango'}
fruits.add('orange')
fruits.remove('banana')
fruits.discard('grapes')
#print(fruits)

#! 3. Common hobbies
A = {'reading', 'gaming', 'music'}
B = {'gaming', 'travel', 'music'}

common = A & B

#print(common)

#! 4. Course Enrollment
#? Using the same A and B above, find hobbies that belong to A but not B, then find hobbies that belong to either group but not both.

Aonly = A-B
#print(Aonly)

either = A^B
#print(either)

#!5. Unique even numbers

#? Given numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 8], create a set containing only the unique even numbers. Try using a set comprehension.

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 8]
unique_even_numbers = {n for n in numbers if n % 2 == 0}

#print(unique_even_numbers) 

#!6. Duplicate detector

#? Write a function has_duplicates(items) that returns True if a list contains duplicate elements and False otherwise. Hint: compare the length of the list with the length of its set.

def has_duplicates(items):
    listItems = items 
    setItems = set(listItems)


    if(len(setItems) == len(listItems)):
        return False
    else:
        return True

#print(has_duplicates([1,2,3,4]))

#! 7.Student comparison
#?Given python = {'Ram', 'Sita', 'Hari', 'Gita'} and java = {'Sita', 'Gita', 'Mina'}, find (1) students learning both languages, (2) students learning only Python, (3) students learning only one of the two languages, and (4) the total number of unique students.

python = {'Ram', 'Sita', 'Hari', 'Gita'}
java = {'Sita', 'Gita', 'Mina'}
both_lang = python & java
print(f"{both_lang}: are learning both languages")
only_python = python - java
print(f"{only_python}: are learning python language")
only_lang = python ^ java
print(f"{only_lang}: are learning only one language")
unique_students = len(python | java)
print(f"{unique_students}: are total unique students")
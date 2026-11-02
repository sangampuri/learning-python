
# Adding and removing elements from a set

students = {"John", "Alice", "Bob"}
students.add("Hari")
#print(students)

#!Removig elements  from set
students = {"John", "Alice", "Bob"}
students.remove("Bob")
#print(students)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
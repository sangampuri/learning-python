A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))    # True
print(B.issuperset(A))  # True
print(A.isdisjoint({5, 6}))  # True

#? issubset() checks whether every element of the first set exists in the second.

#? issuperset() checks whether the set contains every element of another set.

#? isdisjoint() checks whether two sets have no elements in common.


# Looping through a set
countries = {"USA", "Canada", "Germany", "France", "Italy", "Spain", "Australia", "Japan", "China", "India"}

for key,country in sorted(enumerate(countries,1)):
    print(f"{key}: {country}")
#Set union in python
def union(set1, set2):
    return set1 | set2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = union(set1, set2)
print(result)
n=int(input("number of inputs: "))
for i in range(n):
    element = int(input("Enter element: "))
    set1.add(element)
print(set1)
result = union(set1, set2)
print(result)
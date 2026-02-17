#Set intersection in python
def intersection(set1, set2):
    return set1 & set2 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = intersection(set1, set2)
print(result)
n=int(input("number of inputs: "))
for i in range(n):
    element = int(input("Enter element: "))
    set1.add(element)
print(set1)
result = intersection(set1, set2)
print(result)
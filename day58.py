#Remove common elements from list
def remove_common_elements(list1, list2):
    return list(set(list1) - set(list2))
#Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = remove_common_elements(list1, list2)
print(result)
n=int(input("number of inputs: "))
for i in range(n):
    element = int(input("Enter element: "))
    list1.append(element)
print(list1)
result = remove_common_elements(list1, list2)
print(result)
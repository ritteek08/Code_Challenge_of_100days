#Remove duplicates from list
def remove_duplicates(input_list):
    return list(set(input_list))
numbers = [1, 2, 2, 3, 4, 4, 5]
print("List after removing duplicates:", remove_duplicates(numbers))

n=int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
print("List after removing duplicates:", remove_duplicates(numbers))
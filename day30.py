#Count occurrences in list
def count_occurrences(lst, item):
    return lst.count(item)
numbers = [1, 2, 2, 3, 4, 4, 5]
item_to_count = 2
print(f"Occurrences of {item_to_count} in list:", count_occurrences(numbers, item_to_count))
n=int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
item_to_count = int(input("Enter item to count: "))
print(f"Occurrences of {item_to_count} in list:", count_occurrences(numbers, item_to_count))
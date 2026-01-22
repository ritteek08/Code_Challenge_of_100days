#Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers = [10, 20, 30, 40, 50]
target = 30
result = linear_search(numbers, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
n=int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
target = int(input("Enter target element to search: "))
result = linear_search(numbers, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")

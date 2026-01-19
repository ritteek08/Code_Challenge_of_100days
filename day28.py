#Average of list elements
def average_list(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print("Average of list elements:", average_list(numbers))

n=int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
print("Average of list elements:", average_list(numbers))
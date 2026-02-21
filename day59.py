#List comprehension basics
def square(x):
    return x**2
numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)
n=int(input("number of inputs: "))
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)
print(numbers)
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)
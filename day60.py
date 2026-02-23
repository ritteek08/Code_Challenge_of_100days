#Dictionary comprehension
def square(x):
    return x**2
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: square(num) for num in numbers}
print(squared_dict)
n=int(input("number of inputs: "))
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)
squared_dict = {num: square(num) for num in numbers}
print(squared_dict)
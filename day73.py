#Reduce function in Python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print(sum_of_squares)
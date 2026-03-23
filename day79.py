#Recursive factorial with square root optimization
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_with_sqrt(n):
    if n == 0:
        return 1
    else:
        return math.sqrt(n) * factorial_with_sqrt(n - 1)

number = 5
result = factorial_with_sqrt(number)
print(f"Factorial of {number} with square root optimization is {result}")
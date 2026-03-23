#Recursion basics in Python
print("Recursion basics in Python")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")

print("\nFibonacci sequence using recursion")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n_terms = 10
print(f"Fibonacci sequence up to {n_terms} terms:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
#Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print("Fibonacci Series Generator")
n = int(input("Enter the number of terms: "))
print(fibonacci(n))
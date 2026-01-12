#Greatest Common Divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a=int(input("Enter first number to find GCD: "))
b=int(input("Enter second number to find GCD: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")
#Least Common Multiple
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
a=int(input("Enter first number to find LCM: "))
b=int(input("Enter second number to find LCM: "))
print("LCM of", a, "and", b, "is:", lcm(a, b))
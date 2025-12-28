#Find largest of three numbers
print("Find largest of three numbers")
a=int(input("Enter the first variable (a):"))
b=int(input("Enter the second variable (b):"))
c=int(input("Enter the third variable (c):"))

if a>=b and a>=c:
    print("a is the largest number")
elif b>=a and b>=c:
    print("b is the largest number")
else:
    print("c is the largest number")
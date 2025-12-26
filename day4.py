#Code9
#Convert Celsius to Fahrenheit
print("Celsius to Fahrenheit Converter")
c=int(input("Enter temperature in Celsius (°C): "))
f=(c*9/5)+32
print(f"The temperature in Fahrenheit is: {f:.2f} °F\n")

#Code10
#Swap Two Numbers
print("Swap Two Numbers")
x= float(input("Enter first number (x): "))
y= float(input("Enter second number (y): "))
x, y = y, x
print(f"After swapping, first number (x): {x}, second number (y): {y}\n")

#Code11
#Check Even or Odd
print("Check Even or Odd")
num= int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is Even\n")
else:
    print(f"{num} is Odd\n")
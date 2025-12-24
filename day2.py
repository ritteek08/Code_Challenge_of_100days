#Code4
#Simple interest calculator
print("To Simple interest calculator")
print("Enter the details given in the following:\n")

p=float(input("Enter the Principle amount: ₹"))
r=float(input("Enter the rate of interest (per year, in %): "))
t=int(input("Enter the Time period (in year): "))
si=(p*r*t)/100
print(f"\nSimple interest profit amount: ₹{si:3f}")
print("Final amount value with interest: ₹",round(p+si,3),"\n")

#Code5
#Component interest calculation
print("To Component interest calculator")
print("Enter the details given in the following:\n")

p=float(input("Enter the Principle amount: ₹"))
r=float(input("Enter the rate of interest (per year, in %): "))
t=int(input("Enter the Time period (in year): "))
ci=(p*((1+(r/100))**t))-p
print(f"\nComponent interest profit amount: ₹{ci:3f}")
print("Final amount value with interest: ₹",round(p+ci,3),"\n")
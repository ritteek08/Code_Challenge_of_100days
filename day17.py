#Armstrong number
def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == n

# Test the function
print("Checking the number 153 is armstrong number:",is_armstrong_number(153))  # Should return True
print("Checking the number 123 is armstrong number:",is_armstrong_number(123))  # Should return False


num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
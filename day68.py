# Exception handling in Python
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block will always execute.")
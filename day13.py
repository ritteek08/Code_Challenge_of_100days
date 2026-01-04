#Multiplication table
num = int(input("Enter a number: "))
print(f"Multiplication table for {num}")
end = int(input("Enter a number range: "))
for i in range(1, end + 1):
    print(f"{num} x {i} = {num*i}")

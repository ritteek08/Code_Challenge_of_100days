# Delay Message in Python
import time

message = input("Enter message: ")
delay = int(input("Enter delay in seconds: "))
print(f"Message will be displayed after {delay} seconds...")

for i in range(delay, 0, -1):
    print(f"{i} seconds remaining...", end="\r")
    time.sleep(1)

print(f"\n{message}")
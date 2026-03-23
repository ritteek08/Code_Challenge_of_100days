# Simple Timer Application
print("Welcome to the Simple Timer Application!")
import time

def timer():
    seconds = int(input("Enter the timer duration in seconds: "))
    print()
    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
    print("\nTime's up!")
timer()
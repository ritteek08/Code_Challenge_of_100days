#15-Second Timer with Alarm in Python
import time

print("Timer started (15 seconds)")
for i in range(15, 0, -1):
    print(f"\r{i} seconds remaining", end="")
    time.sleep(1)

print("\n\n TIME'S UP! ")
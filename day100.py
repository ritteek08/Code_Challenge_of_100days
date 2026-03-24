#15-Second Random Dice Roller in Python
import time
import random

print("Random Dice Roller (15 seconds)")
print("Rolling dice every second...\n")

scores = []

for i in range(15):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    scores.append(total)
    
    print(f"\rRoll {i+1:2d} | {dice1} + {dice2} = {total:2d} | {'█' * (total//2)}", end="")
    time.sleep(1)

best = max(scores)
worst = min(scores)
avg = sum(scores) / len(scores)

print(f"\n\n Results:")
print(f"   Best roll: {best}")
print(f"   Worst roll: {worst}")
print(f"   Average: {avg:.1f}")
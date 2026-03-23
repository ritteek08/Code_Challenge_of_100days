#Lottery Number Selector in Python
import random

lottery_numbers = random.sample(range(1, 19), 6)
print(f"Lottery numbers: {lottery_numbers}")

bonus_number = random.randint(1, 36)
print(f"Bonus number: {bonus_number}")
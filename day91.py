#Random Quote Generator in Python
import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Life is what happens to you while you're busy making other plans. - John Lennon"
]

def get_random_quote():
    return random.choice(quotes)

def main():
    print("Random Quote Generator")
    input("Press Enter to get a random quote...")
    print(get_random_quote())

if __name__ == "__main__":
    main()
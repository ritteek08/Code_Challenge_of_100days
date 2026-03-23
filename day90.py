#Age Calculator Tool in Python
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
def main():
    print("Age Calculator Tool")
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    
    birth_date = datetime(year, month, day)
    age = calculate_age(birth_date)
    
    print(f"Your age is: {age} years")

if __name__ == "__main__":
    main()
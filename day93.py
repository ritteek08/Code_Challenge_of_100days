#Basic science Quiz Program in Python
def quiz():
    print("Welcome to the Science Quiz!")
    score = 0
    # Question 1
    answer1 = input("What is the chemical symbol for water? ")
    if answer1.lower() == "h2o":
        score += 1
    # Question 2
    answer2 = input("What planet is known as the Red Planet? ")
    if answer2.lower() == "mars":
        score += 1
    # Question 3
    answer3 = input("What gas do plants absorb from the atmosphere? ")
    if answer3.lower() == "carbon dioxide" or answer3.lower() == "co2":
        score += 1
    print(f"Your final score is: {score}/3")

if __name__ == "__main__":
    quiz()
#Character vowel or consonant
char = input("Enter a character: ")
if char.isalpha() and len(char) == 1:
    if char.lower() in 'aeiou':
        print(char, "is a vowel.")
    else:
        print(char, "is a consonant.")
else:
    print("Please enter a single alphabetic character.")
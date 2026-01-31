#Count consonants in a string
def count_consonants(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
input_string = input("Enter a string: ")
print("Number of consonants in the string:", count_consonants(input_string))
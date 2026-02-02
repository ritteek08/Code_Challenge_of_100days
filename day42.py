#Count lowercase letters
def count_lowercase(input_string):
    count = 0
    for char in input_string:
        if char.islower():
            count += 1
    return count
input_string = input("Enter a string: ")
print("Number of lowercase letters in the string:", count_lowercase(input_string))
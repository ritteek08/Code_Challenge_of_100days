#Count uppercase letters
def count_uppercase(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count
input_string = input("Enter a string: ")
print("Number of uppercase letters in the string:", count_uppercase(input_string))
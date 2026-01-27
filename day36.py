#String length without len()
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
#Example usage
input_string = "Hello, World!"
print(f"Length of the string: {string_length(input_string)}")
#Output: Length of the string: 13
n=input("Enter a string: ")
print(f"Length of the string: {string_length(n)}")
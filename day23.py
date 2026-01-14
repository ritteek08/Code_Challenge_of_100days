#ASCII value of a character
def ascii_value(char):
    return ord(char)
#Example usage
print(ascii_value('A'))  # Output: 65
char=input("Enter a character to find its ASCII value: ")
print("ASCII value of", char, "is:", ascii_value(char))
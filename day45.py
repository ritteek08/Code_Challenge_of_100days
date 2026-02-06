#Split and join string
def split_and_join_string(text, delimiter):
    # Split the string into a list of substrings
    substrings = text.split(delimiter)
    # Join the list of substrings back into a single string with a space as the separator
    joined_string = ' '.join(substrings)
    return joined_string
text = input("Enter a string: ")
delimiter = input("Enter the delimiter to split the string: ")
result = split_and_join_string(text, delimiter)
print("Updated text:", result)
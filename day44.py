#Replace substring
def replace_substring(text, old_substring, new_substring):
    return text.replace(old_substring, new_substring)

text = input("Enter a string: ")
old_substring = input("Enter the substring to be replaced: ")
new_substring = input("Enter the new substring: ")
result = replace_substring(text, old_substring, new_substring)
print("Updated text:", result)
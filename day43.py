#Find substring
def find_substring(text, substring):
    if substring in text:
        return True
    else:
        return False

text = "Hello, my name is John"
substring = "name"

text=input("Enter a string: ")
substring=input("Enter a substring to search for: ")
if find_substring(text, substring):
    print(f'The substring "{substring}" was found in the text.')
else:
    print(f'The substring "{substring}" was not found in the text.')
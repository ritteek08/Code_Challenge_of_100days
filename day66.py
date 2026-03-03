#Count characters in file in python
f = open("test.txt", "r")
content = f.read()
char_count = len(content)
print(f"Number of characters in the file: {char_count}")
f.close()

with open("test.txt", "r") as f:
    content = f.read()
    char_count = len(content)
    print(f"Number of characters in the file: {char_count}")
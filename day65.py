#Count words in file in python
f = open("test.txt", "r")
content = f.read()
word_count = len(content.split())
print(f"Number of words in the file: {word_count}")
f.close()

with open("test.txt", "r") as f:
    content = f.read()
    word_count = len(content.split())
    print(f"Number of words in the file: {word_count}")
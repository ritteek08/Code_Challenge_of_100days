#Find longest word in file in python
f = open("test.txt", "r")
content = f.read()
words = content.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)
f.close()

with open("test.txt", "r") as f:
    content = f.read()
    words = content.split()
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
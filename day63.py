#Append to file in python
f = open("test.txt", "a")
f.write("\nThis is an appended line.")
f.close()
with open("test.txt", "a") as f:
    f.write("\nThis is another appended line.\n")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
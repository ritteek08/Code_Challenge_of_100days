#File write in python
f = open("test.txt", "w")
f.write("This is a test file.")
f.close()
with open("test.txt", "w") as f:
    f.write("\nThis is a test file.\n")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
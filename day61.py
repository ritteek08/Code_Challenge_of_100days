#File read in python
f = open("test.txt", "r")
print(f.read())
f.close()
print("\n")
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
print("\n")
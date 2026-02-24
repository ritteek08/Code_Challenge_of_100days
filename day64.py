#Count lines in file in python
f = open("test.txt", "r")
print(f.read())
f.close()

f=  open("test.txt", "r")
lines = f.readlines()
line_count = len(lines)
print(f"Number of lines in the file: {line_count}\n")

with open("test.txt", "r") as f:
    lines = f.readlines()
    line_count = len(lines)
    print(f"Number of lines in the file: {line_count}")
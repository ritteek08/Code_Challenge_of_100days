#Reverse string
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
s=input("Enter a string: ")
print(f"Reversed string: {reverse_string(s)}")
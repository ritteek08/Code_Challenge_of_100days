#Remove spaces
def remove_spaces(string):
    return string.replace(" ", "")
#Test the function
input_string = "Hello World"
result = remove_spaces(input_string)
print(result)  # Output: HelloWorld

string=input("Enter a string: ")
result = remove_spaces(string)
print("The string without spaces is:", result)
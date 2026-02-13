#Tuple basics
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Access first element
print(my_tuple[-1]) # Access last element
print(len(my_tuple)) # Length of tuple
n=int(input("number of inputs: "))
for i in range(n):
    element = input("Enter element: ")
    my_tuple += (element,)  # Add element to tuple
print(my_tuple)
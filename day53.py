#Convert list to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)
n=int(input("number of inputs: "))
for i in range(n):
    element = input("Enter element: ")
    my_tuple += (element,)  # Add element to tuple
print(my_tuple)
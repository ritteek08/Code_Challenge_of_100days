#Convert tuple to list
def tuple_to_list(tup):
    print(tup)
    return list(tup)
my_tuple = (1, 2, 3, 4, 5)
my_list = tuple_to_list(my_tuple)
print(my_list)
n=int(input("number of inputs: "))
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)
print(my_list)
print(list(my_list))
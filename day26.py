#Smallest element in list
def smallest_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

#Example usage
numbers = [3, 5, 2, 8, 1]
print("The smallest element is:", smallest_element(numbers))
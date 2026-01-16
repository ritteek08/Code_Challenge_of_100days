#Largest element in list
def largest_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
#Example usage
numbers = [3, 5, 2, 8, 1]
print("The largest element is:", largest_element(numbers))
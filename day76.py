#"*args demo in python"
print("Sum of all numbers using *args")
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3))
print(sum_all(4, 5))

#greatest of three numbers using *args
print("\nFind greatest of three numbers")
def greatest_of_three(*args):
    if len(args) != 3:
        return "Please provide exactly three numbers."
    return max(args)
print(greatest_of_three(10, 20, 5))
print(greatest_of_three(7, 3, 9))
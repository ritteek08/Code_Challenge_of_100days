#Filter function in Python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
names = ["Alice", "Bob", "Charlie", "David"]
names_with_a = list(filter(lambda name: 'a' in name.lower(), names))
print(names_with_a)
names_with_c = list(filter(lambda name: 'c' in name.lower(), names))
print(names_with_c)
#Map function in Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("\nSquared Numbers:", squared_numbers, "\n")

names = ["Alice", "Bob", "Charlie"]
greeted_names = list(map(lambda name: f"Hello, {name}!", names))
print("Greeted Names:", greeted_names,"\n")
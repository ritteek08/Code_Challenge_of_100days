#**kwargs demo in python
print("Using **kwargs to display person's information")

def display_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_person_info(name="Alice", age=30, city="New York")

print("\nUsing **kwargs to calculate total price of items")
def calculate_total_price(**kwargs):
    total_price = 0
    for item, price in kwargs.items():
        total_price += price
    return total_price

total = calculate_total_price(apple=1.5, banana=0.75, orange=1.25)
print(f"Total price: {total}")
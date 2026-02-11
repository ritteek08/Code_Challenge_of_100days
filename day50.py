#Update dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict['name'])
print(my_dict.get('age')) 
my_dict['email'] = 'alice@example.com' 
my_dict['age'] = 31 
print(my_dict)
user_key = input("Enter the key you want to update: ")
if user_key in my_dict:
    new_value = input(f"Enter the new value for '{user_key}': ")
    my_dict[user_key] = new_value
    print("Dictionary updated:", my_dict)
else:    print(f"Key '{user_key}' not found in the dictionary.")
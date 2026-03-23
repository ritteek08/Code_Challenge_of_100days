# Password strength checker in Python
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    types = [
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ]
    count = sum(types)
    if count == 4:
        return "Strong: Excellent"
    elif count >= 2:
        return "Medium: Could be stronger"
    else:
        return "Weak: Too simple"
password = input("Enter password: ")
print(check_password_strength(password))
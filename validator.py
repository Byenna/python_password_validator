def validate_password(password):
    if len(password) < 8:
        return ("Password must be at least 8 characters long")
    if not any(char.isupper() for char in password):
        return("Password must contain at least one uppercase letter")
    return "Password is valid!"

password = input("Please enter a password: ")
print(validate_password(password))
def validate_password(password):
    if len(password) < 8:
        return ("Password must be at least 8 characters long")

    return "Password is valid!"

password = input("Please enter a password: ")
print(validate_password(password))
# python_password_validator
Exercise to practice string operations

Sure! Here's a beginner's exercise to practice string operations in Python:
Exercise: Password Validator
Write a program that prompts the user to enter a password and then validates that password using the following criteria:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one digit.
- The password must contain at least one special character from the following list: !@#$%^&*()
If the password passes all the criteria, display a message stating that the password is valid. Otherwise, display a message stating what criteria the password fails to meet.
Note: Python provides useful string methods such as `isalnum()`, `isalpha()`, `isdigit()`, and `islower()` that can be used to check if a string meets certain criteria.
Here's a possible solution:

```
import re

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*()]", password):
        return "Password must contain at least one special character: !@#$%^&*()"
    
    return "Password is valid!"

# Test the password validator
password = input("Enter a password: ")
print(validate_password(password))
```
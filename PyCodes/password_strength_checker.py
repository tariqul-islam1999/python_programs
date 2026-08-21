"""

Simple Password Strength Checker
--------------------------------
Checks whether password length atleast 8 digits or avobe, and contains
at least 1 uppercase , 1 digit and 1 special char

"""
import string

def is_strong_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special_char = True

    is_strong = has_uppercase and has_digit and has_special_char
    return is_strong

user_password = input("Enter a password: ")
strength = is_strong_password(user_password)
print(f"Password is {'strong' if strength else 'weak'}")
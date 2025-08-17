# Method to check password strength
def is_strong_password(password):
    is_strong = len(password) >= 8  # Boolean: True if password is 8+ chars
    return is_strong

# Get user input
user_password = input("Enter a password: ")

# Check and display result
strength = is_strong_password(user_password)
print(f"Password is {'strong' if strength else 'weak'}")
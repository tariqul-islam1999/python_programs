# Method to check username length
def is_valid_username(username):
    is_valid = len(username) >= 5  # Boolean: True if username is 5+ chars
    return is_valid

# Get user input
username = input("Enter a username: ")

# Check and display result
result = is_valid_username(username)
print(f"Username is {'valid' if result else 'too short'}")
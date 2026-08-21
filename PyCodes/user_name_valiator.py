"""

User Name's length Checker
---------------------------
Chekcs whether a user name's length atleast 6 char. 

"""
def is_valid_username(username):
    is_valid = len(username) >= 6 
    return is_valid

username = input("Enter a username: ")
result = is_valid_username(username)
print(f"Username is {'valid' if result else 'too short'}")
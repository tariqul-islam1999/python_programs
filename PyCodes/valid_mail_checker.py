"""

Valid E-mail Checker
---------------------
Checks whether an email is valid or not

"""
user_mail = input("Enter your mail address - ")

def is_valid_mail(email):
    is_valid="@" in email and "." in email
    return is_valid

result = is_valid_mail(user_mail)
print(f"Your mail is { 'valid' if result else 'Your mail is invalid'} ")
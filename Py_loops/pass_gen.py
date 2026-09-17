"""
Password Generator 
------------------
create a strong random password using for loop according to user's password length

"""
import random
import string

passwordLength = int(input("Length ? : "))

letters = string.ascii_letters + string.digits + string.punctuation

yourPass=""

for i in range(passwordLength):
   yourPass += random.choice(letters)

print(f"Your Password : {yourPass}")


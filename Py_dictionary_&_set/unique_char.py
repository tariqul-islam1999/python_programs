"""
Unique Character Count
-----------------------
checks how many unique characters in user input

"""

user_input = input("Enter the value : ").strip()

unique_char = set(user_input)

print(f"There are {len(unique_char)} unique characters in this text")
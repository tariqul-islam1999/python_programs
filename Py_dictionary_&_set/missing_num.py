"""
Missing Number Identifier
-------------------------
find the missing number from the list

"""

given_list = [1,3,5,7,9]

full_set = set(range(1,11))

given_set = set(given_list)

missing_numbers = full_set.difference(given_set)

print(f"Missing mumbers are {missing_numbers}")
"""

Count Vowels in a String
-------------------------
Count how many vowels in the sentence/word.

"""
messages = input("Enter the text : ")
vowels = "aeiou"
count = 0

for message in messages.strip().lower():
    if(message in vowels.strip().lower()):
        count += 1
print(f"There are {count} vowels in the text")
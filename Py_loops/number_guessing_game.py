"""

Number Guessing Game
---------------------
User guess the number what program thought

"""
import random
secret_number = random.randint(1,50)
print("Guess the number between 1 to 100")

while True:
    guess_number = int(input("Enter guess number : "))

    if guess_number < secret_number:
        print("Too Low! Please try again")

    elif guess_number > secret_number:
        print("Too High! Please try again")

    else:
        print("!! Yeah , That's Correct !!")
        break
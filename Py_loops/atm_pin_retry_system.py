"""

ATM Pin Retry System
---------------------
This program will allow the user gets 3 attems to enter the correct
pin, after 3 wrong attems , the card gets locked. 

"""
correct_pin = "TIFlovesPY@26"
attempts = 0
max_attempts = 3

while attempts< max_attempts:
    user_pin = input("Enter your pin : ")

    if user_pin.strip() == correct_pin:
        print("!! Welcome !!")
        break

    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts

        if remaining_attempts > 0:
            print(f"!! Wrong Pin , You have only {remaining_attempts} attempt left!!")

        else:
            print("Too many wrong attempts !! Your card is locked !!")    


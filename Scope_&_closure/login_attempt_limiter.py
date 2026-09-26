"""
Login Attemp Limiter
---------------------
a mini security system which track the login attemp using closure.

"""

def create_login_limiter(max_attempts = 3):
    correct_password= "Ilovepython@2026"
    attempt_made = 0
    locked = False

    def attempt(user_input):
        nonlocal attempt_made,locked
        if locked:
            print("!! Account is locked !! Contact Support.")
            return
        if(user_input == correct_password):
            print("!! Correct Password !! Logged in.")

        attempt_made += 1
        remaining = max_attempts - attempt_made

        if remaining <= 0:
            locked = True
            print("!! Account Locked !! Too many failed attempts")
        else:
            print(f"!! Wrong Password !! {remaining} attempts left")

    def reset():
        nonlocal attempt_made,locked
        attempt_made = 0
        locked = False
        print("Account Unlocked. Please try with correct password")

    def get_status():
        if locked:
            print(f"Status : LOCKED | Attempts used : {attempt_made}/{max_attempts}")
        else:
            print(f"Status : ACTIVE | Attempts used : {attempt_made}/{max_attempts}")

    return{
        "attempt" : attempt,
        "reset" : reset,
        "get_status" : get_status
    }

#user_pass = input("Enter Your Password : ")

limiter = create_login_limiter(max_attempts=3)

limiter["attempt"]("laura")
limiter["attempt"]("laura")
limiter["attempt"]("laura")
limiter["attempt"]("Ilovepython@2026")

limiter["get_status"]()

limiter["reset"]()
limiter["get_status"]()

limiter["attempt"]("Ilovepython@2026")

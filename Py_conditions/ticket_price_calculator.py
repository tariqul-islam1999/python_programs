"""

Ticket Price Calculator
------------------------
Calculates the ticket price based on "Age Group" & "Day Type"

"""

age = int(input("Enter Your Age : "))
day_type = input("(Weekday / Weekend) ? : ")

if (age < 0):
    print("Age can not be negative")
else:
    if(age <= 12):
        base_price = 100
        category = "Child"
    elif(age <= 59):
        base_price = 200
        category = "Adult"
    else:
        base_price = 120
        category = "Senior"

    if(day_type == "Weekend"): # pice increase in weekend
        final_price = base_price + 50
    else:
        final_price = base_price

    print(f"\nCategory : {category}")
    print(f"Day Type : {day_type}")
    print(f"Ticket Price : {final_price}")

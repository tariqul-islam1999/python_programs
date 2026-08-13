"""

Leap Year Checker
------------------
Checks whether user's entered year is leap year or not

"""
year = int(input("Enter a year : "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print("Not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print("Not a leap year")

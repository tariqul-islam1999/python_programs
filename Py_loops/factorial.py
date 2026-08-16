"""

Factorial
----------
Calculate the factorial of a number

"""
number = int(input("Enter the number : "))
factorail = 1
for i in range(1,number+1):
    factorail = factorail * i
    if(factorail == 0):
        print(f"Factorial of 0 is 1")
print(f"Factorial of {number} is {factorail}")

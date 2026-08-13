"""

Name Checker
------------
Checks whether the entered name exists in a list

"""

names = ["Tariqul","Islam","Faisal"]
your_name = input("Enter your name : ")

if (your_name in names):
    print("You just make the list!")

else:
    print("Not in the list!")
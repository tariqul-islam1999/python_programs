"""

BMI (Bodu Mass Index) Calculator
--------------------------------
This program will calculate the BMI of any person

"""
try:
    weight = float(input("Enter your weight (KG) : "))
    height = float(input("Enter your height (M) : "))

    if(weight <= 0 or height <= 0):
        print("Invalid !! Weight & Height must be positive number")
    else:
        bmi = weight/(height ** 2)
        print(f"Your BMI is : {round(bmi,2)}")
        if(bmi<18.5):
            print("!! You are Underweight !!")
        elif(bmi<25):
            print("!! You are Normal Weight !!")
        elif(bmi<30):
            print("!! You are Overweight !!")
        else:
            print("!! Obese !!")
except ValueError:
    print("Please enter only numeric value !!")
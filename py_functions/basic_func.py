"""
Basic Function Operations
--------------------------
python user define function's basic structure & operations

"""
# without perameters
def avg():
    num1=int(input("1st val : "))
    num2=int(input("2nd val : "))
    num3=int(input("3rd val : "))
    average = (num1+num2+num3)/3
    print(f"Average : {average}")

#avg()

# with perameter
def tem(farenhite):
     celsious = 5*(farenhite-32)/9
     return celsious

farn = float(input("Enter Temp in Farenhite : "))
result=tem(farn)
print(result)
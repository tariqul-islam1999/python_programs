"""

Simple Calculator
------------------
Takes 2 numbers and an operator (+, -, *, /) from the user
and prints the result. Handles invalid operators, invalid
number input, and divison by zero

"""

operator = input("Choose Operators (+, -, *, /) : ").strip()

try:
    num1 = float(input("Enter 1st Value : "))
    num2 = float(input("Enter 2nd Value : "))

    if operator == "+" :
        result = num1 + num2
        print(round(result,2))

    elif operator == "-" :
        result = num1 - num2
        print(round(result,2))

    elif operator == "*" :
        result = num1 * num2
        print(round(result,2))

    elif operator == "/" :
        if num2 == 0 :
            print("!! Can't divide by zero !!")
        else:
            result = num1 / num2
            print(round(result,2))

    else:
        print("Invalid Operator!")

except ValueError:
    print("Not allowed to take any value except numeric value !")
num1=int(input("enter 1st number - "))
num2=int(input("enter 2nd number - "))
action=input("enter action - ")

if action == "add":
    print(num1+num2)

elif action == "sub" :
    print(num1-num2)

elif action == "mul" :
    print(num1*num2)

elif action == "div" :
    print(num1/num2)

else :
    print("invalid")
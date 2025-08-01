num1=int(input("enter 1st number - "))
num2=int(input("enter 2nd number - "))
action=input("enter action - ")

def add():
    print(num1+num2)

def sub():
    print(num1-num2)

def mul():
    print(num1*num2)

def div():
    if num1==0 | num2==0:
     print("number can not be 0")
    else:
        print(num1/num2)

if action == "add":
    add()

elif action == "sub" :
    sub()

elif action == "mul" :
    mul()

elif action == "div" :
    div()

else :
    print("invalid")


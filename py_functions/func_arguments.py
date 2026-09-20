"""
Python Function Arguments
--------------------------
types of python arguments & it's operations

Types of Arguments - 
1. Default Arguments
2. keyword Arguments
3. Variable Length Arguments
4. Required Arguments

"""

# 1. Default Arguments

def add (a=10,b=20):
    return a+b
print(add())

def mul (a=5,b=10):
    print(f"Result - {a*b}")
mul(100,2)

def div (a= 5,b=10):
    print(f"Result - {a/b}")
div(b=2)

# 2. Keyword Arguments

def greet(greeting,message,name):
    print(f"{greeting}, {name}! {message}.")

greet(name="Tariqul",greeting="Good Morning",message="Welcome")

def email(to,greeting,name,message):
    print(f"To : {to}\n{greeting}, {name}!\n{message}.")

email("faysal@gmail.com",name="Tariqul",greeting="Good Evening",message="Tomorrow you will work from office")
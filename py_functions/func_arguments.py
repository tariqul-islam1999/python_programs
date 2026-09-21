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
#---------------------------------------------------------------
def mul (a=5,b=10):
    print(f"Result - {a*b}")
mul(100,2)
#---------------------------------------------------------------
def div (a= 5,b=10):
    print(f"Result - {a/b}")
div(b=2)

# 2. Keyword Arguments

def greet(greeting,message,name):
    print(f"{greeting}, {name}! {message}.")

greet(name="Tariqul",greeting="Good Morning",message="Welcome")
#---------------------------------------------------------------
def email(to,greeting,name,message):
    print(f"To : {to}\n{greeting}, {name}!\n{message}.")

email("faysal@gmail.com",name="Tariqul",greeting="Good Evening",message="Tomorrow you will work from office")

# Variable Length Arguments

def add_numbers(*number):
    return number

nums = add_numbers(12,34,56,645,234,5454,65343,5464)
print(nums) # all the numbers will be in tuple 

#---------------------------------------------------------------

def show_details(**details):
    for key,val in details.items():
        print(f"{key} : {val}")

show_details(name = "Tariqul",age = 26,hobby="coding") # all the data will be in dictonary 

#---------------------------------------------------------------

def details (name,*numbers,fav_lang="C++",**projects):

    print(f"My name is {name}")
    print("My Contact numbers : ")
    for num in numbers:
        print(f" - {num}")

    print(f"My Favorite Programming Language is {fav_lang}")

    print("My Projects are : ")
    for key,val in projects.items():
        print(f"{key} : {val}")

details(
    "Tariqul",
    "018700007","0161600000",
    fav_lang = "PYTHON",
    project1 = "E-Commerce",
    project2 = "Academic Management System"
)
"""

Variable Scopes in Function
----------------------------
understanding the scopes in python & their uses.

There ase 4 types of scopes in python. Such as -
1. Local
2. Global (keyword)
3. Non-Local (keyword) 
4. Build-in

"""

# Local Scope

def example():
    val = 10 # val is a local scope variable 
    print(val)
example()

# Global Scope1
balance=1000
def bank():
    deposit=500
    print(f"New balance - {deposit+balance}") # here balance's value came from global scope
bank()

#------------------------------------------------------

def bank():
    print(f"balance - {balance}") # here function can access the value of global variable
bank()

#-------------------------------------------------------

def bank():
    global balance # for manipulate the global value, we should use (global) keyword. Otherwise we can't
    withdrawal = 300
    balance -= withdrawal
    print(balance)
bank()

#-------------------------------------------------------

# Non-Local Scope

x=10
def outter():
    x=12
    def inner():
        nonlocal x # nonlocal keyword means that one scope out & change the outter function
        x=8
        print(f"from inner {x}") # Here inner x=8 will print 1st , then outter x=8 & last global x=10
        return                  
    inner()
    print(f"from ouuter {x}")
    return
outter()
print(f"from global {x}")
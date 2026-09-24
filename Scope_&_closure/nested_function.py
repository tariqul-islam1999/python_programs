"""
Nested Function (LEGB)
-----------------------
variable scope operations with nested function using (Local, Enclose, Global, Build-in - LEGB)
method

"""
# nested function operations with variable scope
x=10
def outter():
    x=12
    def inner():
        x=8
        print(f"from inner {x}") # Here inner x=8 will print 1st , then outter x=12 & last global x=10
        return                  
    inner()
    print(f"from ouuter {x}")
    return
outter()
print(f"from global {x}")

#--------------------------------------------------------

x=10
def outter():
    x=12
    def inner():
        print(f"from inner {x}") # Here inner x=12 will print 1st , then outter x=12 & last global x=10
        return                  
    inner()
    print(f"from ouuter {x}")
    return
outter()
print(f"from global {x}")

#--------------------------------------------------------

x=10
def outter():
    def inner():
        print(f"from inner {x}") # Here inner x=10 will print 1st , then outter x=10 & last global x=10
        return                  
    inner()
    print(f"from ouuter {x}")
    return
outter()
print(f"from global {x}")

#----------------------------------------------------------

x=10
def outter():
    x=12
    def inner():
        global x
        x=8
        print(f"from inner {x}") # Here inner x=8 will print 1st , then outter x=12 & last global x=8
        return                  
    inner()
    print(f"from ouuter {x}")
    return
outter()
print(f"from global {x}")


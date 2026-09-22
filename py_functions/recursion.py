"""
Recursion in Python Function
-----------------------------
basic recursion & it's operations in python function.

"""
# recursive function
def show (n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(10)

#----------------------------------------

# Factorial Using Recursion

def factorial(num):
    if (num == 1):
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter the val : "))
fact = factorial(num)
print(fact)

# Fibonacci Sequence Using Recursion

def fibonacci(number):
    if(number <= 1):
        return number
    return fibonacci(number-1) + fibonacci (number-2)

val = int(input("Enter the position : "))
fib = fibonacci(val)
print(f"{val}th Fibonacci Number : {fib}")
for i in range(val):
    print(fibonacci(i), end=" ")
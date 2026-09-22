"""
Calculate Factorial
--------------------
calculate factorial of user's input using function.

"""

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

num = int(input("Enter the range : "))
cal_fact(num)
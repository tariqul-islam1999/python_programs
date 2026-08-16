"""

Star Pattern
-------------
Prints a simple triangle pattern of stars

"""

val = int(input(" Value - "))
for i in range(1,val+1):
    print(" " * (val-i), end="")
    print("*" * (2*i-1), end="")
    print("")
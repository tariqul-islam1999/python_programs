"""

Largest & Smallest Number Identifier
------------------------------------
Find the largest & smallest values from the list

"""

numbers =[23,5,343,322424,55,21,25,2026,147570]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num>largest:
        largest = num
    elif num<smallest:
        smallest = num

print(f"List :  {numbers}")
print(f"Largest : {largest}")
print(f"Smallest : {smallest}")

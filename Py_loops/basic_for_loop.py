"""

Basic For loops
----------------
Basic Structure of For-loop

"""
#1
for i in range(0,10):
    print(i)

#2
list = ["Apple", "Orange","Coconut","Lichi"]

for item in list:
    print(item)

#3
words = "ABCDEFGHIJK"
for word in words:
    print(word)

#4
value = int(input("Enter Number : "))
for i in range(1,11):
    print(f"{value} X {i} = {value * i}")
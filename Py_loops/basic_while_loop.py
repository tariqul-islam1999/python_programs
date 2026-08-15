"""

Basic While loops
-------------------
Basic Structure of While-loop

"""
#1
count = 1
while count <= 5:
    print(count)
    count += 1
print("End Program")

#2
limit = int(input("Enter the number range : "))
target = int(input("Enter the target value : "))
count = 0

while count <= limit:
    print(count)
    if(count == target):
        print("Found !")
        break
    count += 1


#3
limit = int(input("Enter the number range : "))
target = int(input("Enter the target value : "))
count = 0

while count <= limit:
    if(count == target):
        print("Found !")
        count += 1
        continue
    print(count)
    count += 1
    
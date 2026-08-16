"""

Multiplication Table
---------------------
Show multiplication table according to the use input range

"""

start = int(input("Enter the Start : "))
end = int(input("Enter the end : "))

for i in range(start,end+1):
    print(f"\n-------- Multiplication of {i} ------------")

    for j in range(1,11):
        print(f"{i} X {j} = {i * j}")
        
    print("-------------------------------------------")
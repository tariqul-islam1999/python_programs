"""

Sum Average Numbers
-------------------
Ask the user how many numbers they want to enter then
calculate the total sum and average

"""

count = int(input("How many numbers ? : "))
total = 0

for i in range(count):
    number = float(input(f"Enter the number {i+1} : "))
    total = total + number

average = total/count

print(f"Sum : {round(total,2)}")
print(f"Average : {round(average,2)}")
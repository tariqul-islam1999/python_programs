"""

Countdown Timer
---------------
This program will takes a number of seconds from the user and
counts down to zero.

"""
import time

count_down_time = int(input("Enter the count down (Second) : "))

while count_down_time > 0 :
    print(f"Time Lef : {count_down_time}...")
    time.sleep(1)
    count_down_time -= 1

print("!! Time's Up !!")
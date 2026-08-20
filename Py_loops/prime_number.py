"""

Prime Number Checker
---------------------
Checks if a number is prime using a while loop

"""

number = int(input("Enter the number : "))

if number <= 1:
    print(f"{number} is not a prime number !!")

else:
    divisor = 2
    is_prime = True

    while divisor < number :
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"{number} is prime number.")
    else:
        print(f"{number} is not prime.") 
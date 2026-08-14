"""

Mini Discount Calculator
--------------------
Calculate the discount amount according to the conditions & calculate the final total.

"""

try:
    total = float(input("Enter the amount : "))

    if(total < 0):
        print("!! Negative amount not allowed !!")
    else:
        if(total < 500):
            discount_percent = 0
        elif(total < 1000):
            discount_percent = 5
        elif(total < 5000):
            discount_percent = 10
        else:
            discount_percent = 20

        discount_amount = (discount_percent/100) * total
        final_price = total - discount_amount

        print(f"\nOriginal Amount : {round(total,2)}")
        print(f"Discount Avail : {discount_percent}%")
        print(f"Final Price : {round(final_price,2)}")

except ValueError:
    print("Invalid !! Only numeric value allowed")
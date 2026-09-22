"""
Currency Converter 
-------------------
Conver the currency (Foreign Currency to BDT and BDT to Foreign Currency) 
using function.

"""

def converter (amount,options,currency="NONE"):
    usd = 122
    euro = 140
    inr = 1.29
    gbp = 164
    sar = 32

    rate = 0
    if currency.upper() == "USD":
        rate = usd
    elif currency.upper() == "EURO":
            rate = euro
    elif currency.upper() == "INR":
            rate = inr
    elif currency.upper() == "GBP":
            rate = gbp
    elif currency.upper() == "SAR":
            rate = sar
    else:
        return "Not Available !"

    if options == 1:
        total_bdt = amount*rate
        return f"{amount} = {total_bdt} BDT"
    elif options == 2:
        total_foreign = amount/rate
        return f"{amount} BDT = {total_foreign} {currency.upper()}"
    else:
        return "Wrong Choice !"

print("============== Currency Converter ==================")
print("1. Foreign Currency To BDT")
print("2. BDT To Foreign Currency")

options = int(input("Enter Your Choice (1 or 2) : "))
user_currency = input("Enter Currency Name : ")
user_amount = float(input("Enter the amount : "))

result = converter(user_amount,options,user_currency)
print(result)
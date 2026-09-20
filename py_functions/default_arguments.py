"""
Default Argument Functions
---------------------------
some problems & usages of default arguemnt functions

"""

# E-Commerec tax & discount calculator

def invoice_total(price, tax_rate = 0.15, discount = 0.0):
    after_discount_price = price - (price*discount)
    final_price = after_discount_price + (after_discount_price*tax_rate)
    return round(final_price,2)

print(f"Regular Invoice Total : {invoice_total(1000)}")
print(f"After Discount Invoice Total : {invoice_total(1500,discount=0.10)}")
print(f"Invoice Total (Non-Taxable): {invoice_total(1200,tax_rate=0.0,discount=0.05)}")


# Server Log Entry Generator

def log_message(message,level="INFO",destination="localhost"):
    formatted_log = f"[{level}] -> {destination} | Msg: {message}"
    return formatted_log

print(log_message("!! User Logged in Successfully !!"))
print(log_message("!! High CPU usage detected !!", level="WARNING"))
print(log_message("!! Database Connection Lost !!", level="ERROR", destination="remote-db-01"))
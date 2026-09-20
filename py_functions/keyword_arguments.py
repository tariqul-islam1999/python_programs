"""
Keyword Arguments in Function
------------------------------
Basic structure & operations of keyword arguments in python function.

"""
# Automated Email Dispatcher
def send_email (to_email,subject,body,priority="NORMAL",retries=0):
    print("=========================================")
    print(f"Recipient   : {to_email}")
    print(f"Subject     : {subject}")
    print(f"Body        : {body}")
    print(f"Priority    : {priority}")
    print(f"Retries     : {retries}")
    print("=========================================")

send_email("user@example.com","Welcome!","Thanks for the joining",)
send_email("admin@example.com","Server Warning","High CPU Usages",priority="HIGH",retries=5)
send_email(
    body="Your Satement is ready.",
    priority="MEDIUM",
    retries=1,
    subject="Bank Statement",
    to_email="tariqul@gmail.com"
)

def filter_products(category,min_price=0.0,max_price=1500.0,brand="ANY",min_rating=0.0):
    return{
        "category"      : category,
        "price_range"   : f"{min_price} - {max_price}",
        "band"          : brand,
        "min_rating"    : min_rating
    }

query1 = filter_products(
    "Laptop",
    min_price=500.0,
    max_price=1200.0,
)
print(f"Query Result : {query1}")

query2 = filter_products(
    "Phones",
    brand="APPLE",
    min_rating=4.5
)
print(f"Query Result : {query2}")
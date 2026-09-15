"""
E-Commerce Price Filter
-----------------------
Filters products based on maximum budget using tuples & list

"""

items = (
    ("Keyboard",1500),
    ("Mouse",700),
    ("Headphone",600),
    ("Pen Drive",550),
    ("Monitor",3000),
    ("Desk Lamp",300)
)

badget = int(input("Enter Your Badget"))
affordable_products = []

for item in items:
    products_name,products_price = item

    if products_price <= badget:
        affordable_products.append(item)

print(f"Affordable Products : {affordable_products}")
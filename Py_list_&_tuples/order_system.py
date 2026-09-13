"""
E-commerce Order System
------------------------
collects order information & item list using nested list & dictionary

"""

orders = []

order_id = input("Enter Order ID : ")
city = input("Enter City Name : ")
street = input("Enter Street Name : ")

item_list = []
item_count = int(input("How many items ?? : "))
inv_total = 0

for i in range(item_count):
    item_name = input("Enter Item Name : ")
    item_price = float(input("Enter Item Price : "))
    inv_total += item_price
    item_list.append({
        "product" : item_name,
        "price" : item_price,
        "inv_total" : inv_total
    })

order = {
    "order_id" : order_id,
    "shipping" : {
        "city" : city,
        "street" : street
    },
    "items" : item_list,
    "inv_total": inv_total
}
orders.append(order)

# Order Summary

print("\n====== Your Cart =======")
print(f"ID : {orders[0]['order_id']}")
print(f"Ship to : {orders[0]['shipping']['city']}, {orders[0]['shipping']['street']}")
print("Purchased Items : ")
for item in orders[0]['items']:
    print(f"{item['product']} : {item['price']}")

print("---------------------")
print(f"Invoice Totla - {orders[0]['inv_total']}")
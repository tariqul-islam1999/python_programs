"""
Shop's Menu Dictionary
-------------------------
Store the item's info in a dictionary. Allows the user add , update or delete any value.

"""
shop = {}

while True:
    print("\n======== Menu ==========")
    print("1. Add Items")
    print("2. Show Items")
    print("3. Update Item")
    print("4. Delete Items")
    print("5. Exit")
    
    choice_options = int(input("Select Option : "))

    if choice_options == 1:
        count_items = int(input("How many items you want to add ? : "))

        for i in range(count_items):
            item_name = input("Enter Item's Name : ").strip()
            item_price = float(input("Enter the price : "))
            shop[item_name] = item_price
        print("!! Items added successfully !!")

    elif choice_options == 2:
        sl_no = 1
        for key,value in shop.items():
            print(f"{sl_no}. {key} = {value} ")
            sl_no += 1

    elif choice_options == 3:
        update_itemName = input("Update the name : ").strip()
        update_price = float(input("Update the price : "))
        shop[update_itemName] = update_price
        print("!! Items updated successfully !!")

    elif choice_options == 4:
        delete_item = input("Enter the name : ")
        if delete_item in shop:
            shop.pop(delete_item)
        print("!! Items deleted successfully !!")

    elif choice_options == 5:
        print("!! Exit the Program !!")
        break
        
    else:
        print("!! Invalid Choice !!")


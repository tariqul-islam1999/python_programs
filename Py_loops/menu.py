"""

Simple Menu-Driven Program
---------------------------
Shows a menu of options and keeps running the user chooses to exit.

"""
while True:
    print("\n======== Menu ========")
    print("1. Create New User")
    print("2. Show All User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    print("========================")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        print("Exicuting Option 1")
    elif choice == 2:
        print("Exicuting Option 2")
    elif choice == 3:
        print("Exicuting Option 3")
    elif choice == 4:
        print("Exicuting Option 4")
    elif choice == 5:
        print("======= Thank You ========")
        break
    else:
        print("!! Invalid choice, try again !!")
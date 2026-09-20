"""
Mini CRUD System Using Function
--------------------------------
A basic cruding system using python function. Where user can insert students,
show students & remove students. All data stores in a simple list

"""
students=[]

def AddStu():
    addName=input("Enter the name : ")
    students.append(addName)
    print(f"{addName}, Added Successfully !! ")
   
def removeStu():
    removeName = input("Remove any name : ")
    if (removeName in students):
        students.remove(removeName)
        print("Removed Successfully !! ")
    else:
        print(f"{removeName}, Not found in the list !! ")

def showStu():
    if (len(students) != 0):
        for i in range(len(students)):
            print(students[i])

    else:
        print("Empty list !! ")


while True:
    print("===== Mini SMS =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Show Student")
    print("4. Exit")
    print("====== END =======")

    selecteMenu = int(input("Selecte Menu : "))

    if(selecteMenu == 1):
        AddStu()
    if(selecteMenu == 2):
        removeStu()
    if(selecteMenu == 3):
        showStu()
    if(selecteMenu == 4):
        print("Program Ended")
        break
"""

Basic Letter Templete
----------------------
A mini program to fill in a letter template given below with name and date.

"""

name = input("enter name - ")
date= input("enter date - ")
letter = f''' 
        Dear {name} ,\n
        Your are selected ! \n
        {date}
 
 '''
print(letter)

# another way
letter2= '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
 '''
print(letter2.replace("<|Name|>","Faysal").replace("<|Date|>","15.07.2026"))
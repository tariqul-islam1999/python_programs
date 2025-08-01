# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

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
print(letter2.replace("<|Name|>","Faysal").replace("<|Date|>","31.07.2025"))
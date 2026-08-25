"""
Python - Nasted Dictionary Basic
---------------------------------
basic operations of nasted dictionary.

"""
nestedDic = {
    "CSE" : {
        "CSE101" : "Structured Programming Language",
        "CSE201" : "Object Oriented Programming",
        "CSE301" : "Database Management"
    },
    "BBA" :{
        "BBA101" : "Introduction to Businness Adminastration",
        "BBA201" : "Management",
        "BBA301" : "Accounting"
    },
    "LAW" :{
        "LAW101" : "Introduction to LAW",
        "LAW201" : "High Court"
    }
}

print(nestedDic) # print full nested dictionary
print(nestedDic["BBA"]) # print any full sub dictionary
print (nestedDic["CSE"]["CSE301"]) # print any value of keys from any perticular sub dictionary

# adding values

nestedDic["EEE"] = {
    "EEE101" : "Introduce to Electrical",
    "EEE201" : "Circutes"
} # add a sub-dictionary into parent dictionary
print(nestedDic["EEE"])

nestedDic["BBA"]["BBA401"] = "HR & Admin" # add a new key-value pair inside any sub-dictionary
print(nestedDic["BBA"])

# delete values
removeCrs = nestedDic["LAW"].pop("LAW201") # delete any key-value pair from sub-dictionary
print(nestedDic["LAW"])

removeDept = nestedDic.pop("LAW") # delete entire sub-dictionary
print(nestedDic)


books = {
    'BK100' : 'Animal Planet',
    'BK101' : 'Trees Voice',
    'BK103' : 'The King of Jungle',
    'BK104' : 'The Birds'
}
copyBooks = books.copy() # copy whole dictionary
print(copyBooks)

print(books.clear()) # Empty full dictionary but variables still exists
del copyBooks # delete full dictonary from memory (RAM)
print("copyBooks deleted!")

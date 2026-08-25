"""
Python - Dictionary Basic
--------------------------
1. Mutable
2. Don't allow duplicate keys
3. keys are immutable
4. values can be duplicate
"""

books = {
    'BK100' : 'Animal Planet',
    'BK101' : 'Trees Voice',
    'BK103' : 'The King of Jungle',
    'BK104' : 'The Birds'
}

commicBooks = {
    "CM101" : "Jungle Pe Mangal",
    "CM102" : "Sapak"
}

moreBooks = {
    "TG101" : "Tiger is alive",
    "TG102" : "Tigers in BD",
    "TG103" : "Mighty Tigers"
}

books['BK105'] = 'Royal Bengal Tiger' # add items into the dictionary
books.pop('BK101') # remove items from the dictionary
print(books) # print the whole dictionary
merged = books | moreBooks # merged two dictionaries
print (merged)

# dictionary methods

print(books.keys()) # shows all the keys
print(books.values()) # shows all the values
print(books.items()) # shows keys & values together
print(books.get("BK100")) # shows particular value & if not is dictionary then it will show (None)
books.update(commicBooks) # update the dictionary with the other dictionary's value
print(books)

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

friends = {}

name = input("enter name - ")
lang = input("enter language name - ")
friends.update({ name : lang })

name = input("enter name - ")
lang = input("enter language name - ")
friends.update({ name : lang })

name = input("enter name - ")
lang = input("enter language name - ")
friends.update({ name : lang })

name = input("enter name - ")
lang = input("enter language name - ")
friends.update({ name : lang })

print(friends)
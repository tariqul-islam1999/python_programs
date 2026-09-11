"""
List Methods
-------------
uses of list methods

"""
new_list = []
new_list.append("tariqul") # adding value in the list
print(new_list)

nums = [4,6,9,10,15,3]
more_nums = [131,256,512,404]
nums.insert(3,101) # insert item in specific position
nums.extend(more_nums) # extended a list with another list
nums.remove(404) # remove speific item by value 
nums.pop(2) # remove speific item by key 
nums.sort() # sorting the all items inside list
print (nums) 

new_list.clear() # clear all the item inside list
print(new_list)

fruits = ["apple" , "banana","lichi","pepe","apple", "pepe","apple"]
print(fruits.index("pepe")) # returns the position of this item in list
print(fruits.count("apple")) # returns how many time this item appears in the list

new_fruits = fruits.copy()
print(new_fruits)




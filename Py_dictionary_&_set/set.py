"""

Basic Set Operations
---------------------
set's basic structure , adding elements , removing elements , cleaning the set 
& others operations.

Rules -  
1. Mutable 
2. allows different types of data type
3. duplicate elements not allowed 
4. Unordered 

"""
emptySet=set() # empty set
emptySet.add(6) # for adding value into set
emptySet.add(10)
emptySet.add(20)

emptySet.remove(6) # for remove an elements from set
emptySet.clear() # for erase every elements from set

print(emptySet)

my_set = {5,10,"a",True,15.667}
my_set.add("nw")
my_set.remove(5)
print(my_set)
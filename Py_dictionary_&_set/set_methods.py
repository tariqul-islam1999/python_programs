"""
Set Methods
-----------
uses of set methods.

"""

first_set = {12,15,17,3,54,7,11,5}
second_set = {210,18.512,3,11,21,1}

print(first_set.union(second_set)) # union operation, which collects all the values from both sets
print(second_set.intersection(first_set)) # intersection operation, which collects only the common values from both sets
first_set.intersection_update(second_set) # Modifies the set in-place, keeping only elements found in both the set and all provided iterables.
print(first_set)

s1 = {1,2,3,4}
s2= {5,6,7,8}
s1.update(s2) # update values into another set
s1.discard(190) # Removes a specific element from the set if it exists otherwise it does not raise an error
print(s1)

removed_value = s2.pop() # Removes and returns an arbitrary element from the set.
print(removed_value)
print(s2)

a= {10,20,30,40}
b= {40,50,60}

print(a.difference(b)) # collect only the values which has in a set but not in b 
print(b.difference(a)) # collect only the values which has in b set but not in a
print(a.symmetric_difference(b)) # collect only the values which is not available in both sets

c = a.copy()
print(c) # copy the whole set

a.difference_update(b) # collect & update in set "a" only the values which not in "b" set
print(a)
b.symmetric_difference_update(a) # collect & update in set "b" only the values which not in both sets
print(b)

cities1 = {"Dhaka", "Delhi","Colombo","Kathmandu"}
cities2 = {"Berlin", "Paris","Rome","Lisbon"}
cities3 = {"Dhaka", "Delhi","Colombo","Kathmandu","Berlin","Rome","Lisbon"}
print(cities1.isdisjoint(cities2)) # return true/false if both sets has no common items
print(cities2.issubset(cities3)) # return true/false if every elements of the set in another set
print(cities3.issuperset(cities1)) # return true/false if every elements of the set in another set

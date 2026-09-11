"""
List Comprehension
-------------------
uses of list comprehension & it's operations.

"""
lst = [i for i in range(11)] # create & add values from 0-10 using a loop inside list
print(lst)

lst2 = [i for i in range(20) if i%2 == 0] # create & add values using loop & condition
print(lst2)

nums = [2,4,5,6,7,3]
lst3 = [n**2 for n in nums]

print(lst3)

names = ["tariqul","faisal","islam","jafrin","luna"]
new_names = [name.title() for name in names]
print(new_names)

mod_names = [name.title() for name in names if len(name)>= 5]
print (mod_names)


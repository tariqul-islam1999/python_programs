"""
List Basic Structure & Operations
----------------------------------
uses of list & it's operations.

Rules - 
1. Mutable
2. Similar key not allowed
3. Multiple data type allowed
4. Ordered

"""

list=["name1","name2",10,96.55,True]
list2=[1,3,5,8,6,7,71,24,9]

list[0]="tariqul" # can change the value at the particular key
list[1]="faysal"

list.remove(True) # for remove any value from list
list.append("Python") # append () add value in the list at the end

list.append("name3")
list[5] = "islam"

print(list2[-3]) # reverse index
print(list) # print whole list
print(list2[3:]) # print values starting from particular key.
print(list2[:-1]) # it will print starting from index "0" if left side of : is blank
print(list2[0:7:2]) # jump index. it takes 1st value first then take 2nd value till the mentioned index
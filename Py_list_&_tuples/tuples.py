"""
Tuples Basic
------------
basic structure & operations of tuples

Rules -
1. Immutable 
2. All data type allowed
3. Ordered
4. Allowed duplicate values
5. Can manipulate the values indirectly

"""

values=("cricket",220,True,10.59,"cricket",54,"football","cricket")
print(type(values),values)
print(values.count("cricket")) # count how many times a value exist in a tuple
print(values.index("football")) # count the index number of any item in tuple
print(values.index(54,4,7)) # index slicing

# Manipulating Tuples - 1

countries = ("Bangladesh","India","Pakistan","Nepal","Bhutan")
temp = list(countries)
temp.append("Maldivs")
temp.pop(1)
countries = tuple(temp)
print(countries)

# Manipulating Tuples - 2

south_asia = ("Bangladesh","India","Pakistan")
south_east_asia = ("Vietnam","China","Singapore")
middle_east = ("Saudi","Oman","Qatar")
asia = south_asia + south_east_asia + middle_east
print(asia)
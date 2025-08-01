# Check that a tuple type cannot be changed in python.

value = (10,20,30,40,55)
value[1]=100 # can not change the tuple
print(value)
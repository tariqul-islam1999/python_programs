"""
Update Value From Two Dictionary
---------------------------------
merge & update the maximum value with the same keys.

"""

first_dict = {
    "Apple" : 120.25,
    "Banana" : 35,
    "Mango" : 80.25,
    "Lichi" : 37 
}

second_dict = {
    "Apple" : 120,
    "Banana" : 35.85,
    "Mango" : 90,
    "Lichi" : 32,
    "Pepe" : 15
}

marged_dict = first_dict.copy()

for key,value in second_dict.items():
    if key in marged_dict:
        marged_dict[key] = max(marged_dict[key],value)
    else:
        marged_dict[key] = value

print("Marged Dictionary : ", marged_dict)
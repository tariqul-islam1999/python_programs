marks ={
    "math" : 80,
    "english" : 90,
    "history" : 70,
    "bangla" : 75
}
print(marks["bangla"])

print (marks, type(marks)) # for checking the type

print(marks.items()) # for view the dictionary into tuple form

print(marks.keys()) # for view only keys from dictionary

print(marks.values()) # for view only values from dictionary

marks.update({"bangla" : 78,"physics" : 65}) # for update the dictionary value

print(marks)

print(marks.get("biology")) # for checking that the keys exist in the dictionary or not


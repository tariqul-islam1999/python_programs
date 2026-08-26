"""
Grading System
---------------
Stores each student's subject-wisemarks using a nested dictionary.
And calculate average marks of each students & topper among them.

"""

students_info = {}

# enter the values in nested dictionary
students_count = int(input("How many student? : "))
total_subject = int(input("How many subject for each student? : "))

for i in range(students_count):
    student_id = input("Enter the ID : ")
    students_info[student_id] = {}
    

    for j in range(total_subject):
        subject_name = input("Enter subject name : ")
        subject_marks = float(input("Enter Marks : "))
        students_info[student_id][subject_name] = subject_marks

# calculate average points for each students 
top_student = ""
top_average = -1
for student in students_info:
    subjects = students_info[student]

    total = 0
    subject_count = 0
    for subject in subjects:
        total = total + subjects[subject]
        subject_count += 1 

    average = total/subject_count
    print (f"\n Student ID : {student}")
    print(f"{subject} : {subjects[subject]}")
    print(f"Average : {round(average,2)}")

# calculate the topper

    if average>top_average:
        top_average = average
        top_student = student

print(f"\nTop Student : {top_student}")
print(f"Highest Average : {top_average}")
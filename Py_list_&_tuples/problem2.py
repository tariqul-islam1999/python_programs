#  Write a program to accept marks of 6 students and display them in a sorted
# manner

marks=[]

stu1=float(input("enter mark - "))
marks.append(stu1)

stu2=float(input("enter mark - "))
marks.append(stu2)

stu3=float(input("enter mark - "))
marks.append(stu3)

stu4=float(input("enter mark - "))
marks.append(stu4)

stu5=float(input("enter mark - "))
marks.append(stu5)

stu6=float(input("enter mark - "))
marks.append(stu6)

marks.sort()
print(marks)
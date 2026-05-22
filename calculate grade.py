#A school wants to calculate grades for students based on marks obtained in five subjects. 
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total_marks = sum(marks)
average_marks = total_marks / 5
if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"The average marks are: {average_marks}")
print(f"The grade is: {grade}")

#output:
# Enter marks for subject 1: 56
# Enter marks for subject 2: 65
# Enter marks for subject 3: 85
# Enter marks for subject 4: 88
# Enter marks for subject 5: 69
# The average marks are: 72.6
# The grade is: C
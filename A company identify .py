# A company wants to identify whether an employee is eligible for a bonus based on attendance percentage and performance rating. 
attendance_percentage=float(input("Enter the attendance percentage: "))
performance_rating=float(input("Enter the performance rating (1-5): "))
if attendance_percentage>=70 and performance_rating>=4:
    print("Employee is eligible for a bonus.")
else:
    print("Employee is not eligible for a bonus.")

# output:
# Enter the attendance percentage: 75
# Enter the performance rating (1-5): 4.5
# Employee is eligible for a bonus.
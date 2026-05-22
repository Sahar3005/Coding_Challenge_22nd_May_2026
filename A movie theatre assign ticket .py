#  A movie theatre wants to assign ticket pricing based on age categories such as child, adult, and senior citizen.
age = int(input("Enter the age of the customer: "))
if age < 12:
    print("The ticket price is 200 for Child.")
elif age < 60:
    print("The ticket price is 560 for Adult.")
else:
    print("The ticket price is 700 for Senior Citizen.")

# output:
# Enter the age of the customer: 10
# The ticket price is 200 for Child.

# Enter the age of the customer: 56
# The ticket price is 560 for Adult.
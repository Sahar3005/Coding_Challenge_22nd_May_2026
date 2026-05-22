# A bank wants to calculate simple interest for customers based on principal, rate, and time entered by the user. 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is: ", simple_interest)

# Output:
# Enter the principal amount: 20000
# Enter the annual interest rate (in %): 20
# Enter the time in years: 2
# The simple interest is:  8000.0
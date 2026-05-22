#Write a program to find the largest among three entered sales figures. 
sales1 = float(input("Enter sales figure 1: "))
sales2 = float(input("Enter sales figure 2: "))
sales3 = float(input("Enter sales figure 3: "))
if sales1 >= sales2 and sales1 >= sales3:
    print("The largest sales figure is: ", sales1)
elif sales2 >= sales1 and sales2 >= sales3:
    print("The largest sales figure is: ", sales2)
else:
    print("The largest sales figure is: ", sales3)

# output:
# Enter sales figure 1: 5000
# Enter sales figure 2: 7000
# Enter sales figure 3: 6000
# The largest sales figure is:  7000.0
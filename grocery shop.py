# A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount. Write a program using if...elif...else to display the final amount. 
user_input=float(input("Enter the purchase amount: "))
if user_input>1000:
    discount=user_input*0.1
    final_amount=user_input-discount
    print("Final amount after 10% discount: ",final_amount)
elif user_input>500:
    discount=user_input*0.05
    final_amount=user_input-discount
    print("Final amount after 5% discount: ",final_amount)
else:
    print("No discount applied. Final amount: ",user_input)

# Output:
# Enter the purchase amount: 580
# Final amount after 5% discount:  551.0

# Enter the purchase amount: 5000
# Final amount after 10% discount:  4500.0

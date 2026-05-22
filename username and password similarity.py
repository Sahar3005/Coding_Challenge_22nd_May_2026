#Create a program to check whether a given username and password match predefined credentials. 
predefined_username = "admin"
predefined_password = "password123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == predefined_username and input_password == predefined_password:
    print("Login successful!")
else:
    print("Invalid username or password.")


# output:
# # Enter username: admin
# Enter password: password123
# Login successful!

# Enter username: user
# Enter password: password
# Invalid username or password.
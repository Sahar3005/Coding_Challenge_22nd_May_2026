#Create a login attempt system that allows the user a maximum of 3 attempts using a while loop.
predefined_username = "admin"
predefined_password = "password123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username == predefined_username and input_password == predefined_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Invalid username or password. Attempt {attempts} of {max_attempts}.")

# output:
# Enter username: user
# Enter password: password
# Invalid username or password. Attempt 1 of 3.
# Enter username: admin
# Enter password: pass
# Invalid username or password. Attempt 2 of 3.
# Enter username: admin
# Enter password: password123
# Login successful!

# Enter username: admin
# Enter password: password
# Invalid username or password. Attempt 1 of 3.
# Enter username: admin
# Enter password: pass
# Invalid username or password. Attempt 2 of 3.
# Enter username: admin
# Enter password: pass123
# Invalid username or password. Attempt 3 of 3.
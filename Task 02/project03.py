# Simple Login System: Validate user credentials
def login_system():
    # Stored credentials
    stored_user = "admin"
    stored_pass = "1234"
    
    # User input
    username = input("Username: ")
    password = input("Password: ")
    
    # Validation
    if username == stored_user and password == stored_pass:
        print("Login Successful")
    else:
        print("Login Failed: Invalid credentials")

# Run the program
login_system()
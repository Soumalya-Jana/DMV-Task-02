# User Login Validation System
def validate_login(username, password, account_locked):
    db_user = "admin"
    db_pass = "secure123"
    
    if username == db_user and password == db_pass and not account_locked:
        return "Login successful. Welcome back!"
    
    elif account_locked:
        return "Error: Account is currently locked. Please contact support."
    else:
        return "Error: Invalid username or password."

print(validate_login("admin", "secure123", False)) 
print(validate_login("admin", "wrongpass", False))  
print(validate_login("admin", "secure123", True))   
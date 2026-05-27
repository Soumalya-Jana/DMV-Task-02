# This function checks if a password is strong enough based on its length.
def is_password_strong(password):
    # Returns True if it's 8 or more characters, False otherwise
    if len(password) >= 8:
        return True
    else:
        return False

user_input = "pass123"

# Because the function evaluates to True or False, it acts like a condition
if is_password_strong(user_input):
    print("Account created successfully.")
else:
    print("Error: Password must be at least 8 characters long.")
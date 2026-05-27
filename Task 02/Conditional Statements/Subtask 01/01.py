#Check whether a number is positive or negative
def check_number_sign():
    try:
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is positive.")
        elif num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
check_number_sign()

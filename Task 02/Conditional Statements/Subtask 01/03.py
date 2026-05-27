# This program checks if a number is even or odd.
def check_even_odd():
    try:
        # Prompt the user for a number
        num = int(input("Enter a number: "))
        
        # Check if the remainder is 0 when divided by 2
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
            
    except ValueError:
        print("Please enter a valid whole number.")

# Run the program
check_even_odd()
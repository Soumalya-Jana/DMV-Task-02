# Factorial Calculator: Calculate the factorial of a number
def calculate_factorial(n):
    # Handle edge cases for 0 and negative numbers
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    
    # Calculate factorial
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result

# Run the program
try:
    num = int(input("Enter Number: "))
    fact = calculate_factorial(num)
    print(f"Factorial: {fact}")
except ValueError:
    print("Please enter a valid whole number.")
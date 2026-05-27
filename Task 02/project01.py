# Grade Calculator: Calculate grade based on marks
def calculate_grade():
    try:
        marks = float(input("Enter Marks: "))
        
        if marks >= 90:
            print("Grade: A+")
        elif marks >= 75:
            print("Grade: A")
        elif marks >= 60:
            print("Grade: B")
        else:
            print("Grade: C")
            
    except ValueError:
        print("Please enter a valid number.")

# Run the program
calculate_grade()
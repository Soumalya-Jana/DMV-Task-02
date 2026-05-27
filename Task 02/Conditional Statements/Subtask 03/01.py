# Grade Classification System
def classify_grade(score):
    print(f"Evaluating score: {score}")
    
    if score >= 90:
        return "Grade: A"
    elif score >= 80:
        return "Grade: B"
    elif score >= 70:
        return "Grade: C"
    elif score >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

print(classify_grade(85))  
print(classify_grade(92))  
print(classify_grade(45))  
# Scholarship Eligibility Evaluator
def evaluate_scholarship(gpa, extracurriculars, volunteer_hours, has_disciplinary_record):
    
    if gpa >= 3.8 and (volunteer_hours >= 100 or extracurriculars >= 3) and not has_disciplinary_record:
        return "Status: Awarded Full Scholarship!"
    
    elif has_disciplinary_record:
        return "Status: Denied. Disciplinary records disqualify applicants."
        
    else:
        return "Status: Denied. Did not meet academic or community requirements."

print(evaluate_scholarship(3.9, 1, 150, False)) 

print(evaluate_scholarship(4.0, 5, 200, True))  

print(evaluate_scholarship(3.9, 1, 20, False))
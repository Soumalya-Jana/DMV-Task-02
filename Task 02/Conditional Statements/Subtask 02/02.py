# University Admission Eligibility Checker
MIN_AGE = 17
MAX_AGE = 25
MIN_MARKS = 60
SCHOLARSHIP_MARKS = 90

applicant_age = int(input("Enter applicant's age: "))
applicant_marks = float(input("Enter high school percentage/marks: "))

if applicant_age >= MIN_AGE:
    if applicant_age <= MAX_AGE:
        print("Age eligibility verified.")
        
        if applicant_marks >= MIN_MARKS:
            print("Academic eligibility verified.")
            
            if applicant_marks >= SCHOLARSHIP_MARKS:
                print("Status: Admitted with a 100% Merit Scholarship!")
            else:
                print("Status: Admitted (Regular Tier).")
                
        else:
            print(f"Status: Rejected. Marks are below the required {MIN_MARKS}%.")
            
    else:
        print(f"Status: Rejected. Applicant exceeds the maximum age limit of {MAX_AGE}.")
else:
    print(f"Status: Rejected. Applicant must be at least {MIN_AGE} years old.")
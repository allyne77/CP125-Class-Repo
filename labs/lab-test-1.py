#allyne lab-test-1.py , kelas C02

#checks student's grade based on mark input
def determine_grade(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade

# User input
mark = float(input("Enter the student's mark: "))
grade = determine_grade(mark)

print("Mark:", mark, ", Grade:", grade)
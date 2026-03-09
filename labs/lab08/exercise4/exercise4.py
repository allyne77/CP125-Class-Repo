# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv
def calculate_final_grades(input_file, output_file):
    midterm = open(input_file, "r", newline="")
    midterm_reader = csv.reader(midterm)
    final = open(output_file, "w", newline="")
    writer = csv.writer(final)

    next(midterm_reader)
    writer.writerow(["student_id", "final_grade"])

    total_grades = 0
    count = 0

    for row in midterm_reader:
        student_id = row[0]
        midterm = float(row[1])
        final = float(row[2])
        final_grade = midterm * 0.4 + final * 0.6
        writer.writerow([student_id, f"{final_grade:.2f}"])
        total_grades += final_grade
        count += 1

    return round(total_grades / count, 2)

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")

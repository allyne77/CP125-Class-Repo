# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    score = open(input_file, 'r')
    passing = open(output_file, 'w')

    passing_students = []

    for line in score:
        student_id, score_str = line.strip().split()
        if int(score_str) >= 80:
            passing_students.append(student_id + " " + score_str + "\n")

    passing.writelines(passing_students)

    score.close()
    passing.close()

    return len(passing_students)

result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")

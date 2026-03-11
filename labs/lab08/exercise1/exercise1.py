# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    passed = []
    scores = open(input_file, 'r')
    passing = open(output_file, 'w')

    count = 0

    while True:
        student_id = scores.readline()
        if student_id == "":
            break

        student_id = student_id[:-1]

        score_line = scores.readline()
        score = int(score_line[:-1])

        if score >= 80:
            passing.write(student_id + " " + str(score) + "\n")
            count += 1

    scores.close()
    passing.close()

    return count



# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")

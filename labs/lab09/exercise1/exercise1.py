import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)
    total_student = len(df)
    subjects = ["Math","Science","English"]
    math_avg = [(df["Math"]).mean() , 1]
    highest_math_student = df.loc[df["Math"].max(), "Name"]

    result = {

        "total_students": total_student,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

result = explore_data("labs/lab09/data/students.csv")
print(result)

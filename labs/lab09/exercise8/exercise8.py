import pandas as pd
import matplotlib.pyplot as plt


def plot_subject_maximums(filename):
    df = pd.read_csv(filename)

    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")

    plt.show()
    return len(df)

count = plot_subject_maximums("labs/lab09/data/students.csv")
# Chart window appears showing line plot of maximum scores
print(count)  # 25
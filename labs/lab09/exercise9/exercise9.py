import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("labs/lab09/data/students.csv")

plt.hist(df['Math'], bins=10, alpha=0.5, label="Math")
plt.hist(df['Science'], bins=10, alpha=0.5, label="Science")
plt.hist(df['English'], bins=10, alpha=0.5, label="English")

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution Comparison")
plt.legend()  # Shows which color is which

plt.show()

# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    f3 = open(output_file, "w")

    lines1 = f1.readlines()
    lines2 = f2.readlines()
    merge = set(lines1 + lines2)
    merged_sorted = sorted(merge)
    f3.writelines(merged_sorted)
    
    return len(merged_sorted)

# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")





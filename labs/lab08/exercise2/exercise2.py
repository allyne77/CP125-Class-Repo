# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    file1 = open(file1, 'r')
    file2 = open(file2, 'r')
    merged = open(output_file, 'w')

    result = []
    list1 = file1.readlines()
    list2 = file2.readlines()

    for name in list1 + list2:
        if name not in result:
            result.append(name)


    merged.writelines(sorted(result))

    file1.close()
    file2.close()
    merged.close()

    return len(result)



# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", 
                     "labs/lab08/exercise2/data/list2.txt", 
                     "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")

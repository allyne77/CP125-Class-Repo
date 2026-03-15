# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv
def summarize_sales(input_file, output_file):
    sales = open(input_file, "r", newline="")
    sales_reader = csv.reader(sales)
    total = open(output_file, "w", newline="")
    total_reader = csv.reader(total)

    next(sales_reader)
    revenues = []
    for row in sales_reader:
        quantity = int(row[1])
        price = float(row[2])
        revenue = quantity * price
        revenues.append(revenue)

    total = sum(revenues)
    average = total / len(revenues)
    highest = max(revenues)
    lowest = min(revenues)

    summary_file = open(output_file, "w")
    summary_file.write(f"Total Revenue: ${total:.2f}\n")
    summary_file.write(f"Average Revenue: ${average:.2f}\n")
    summary_file.write(f"Highest Revenue: ${highest:.2f}\n")
    summary_file.write(f"Lowest Revenue: ${lowest:.2f}\n")

    sales.close()
    summary_file.close()

    return (total, average, highest, lowest)

# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")

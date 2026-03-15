# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    products = open(products_file, "r", newline="")
    product_reader = csv.reader(products)
    order = open(order_file, "r", newline="")
    order_reader = csv.reader(order)
    total = open(output_file, "w")
    writer = csv.writer(total)

    next(product_reader)
    next(order_reader)
    writer.writerow

    products.close()
    order.close()
    total.close()
    return grand_total

result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")


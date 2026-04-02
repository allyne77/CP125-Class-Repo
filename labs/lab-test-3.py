#allyne lab-test-3.py , kelas C02

import csv

def average_height (filename):
    file = open(filename, 'r', newline='')
    reader = csv.reader(file)

    next(reader) #skip

    total_height = 0
    count = 0

    for row in reader:
        total_height = float(row[1])
        count += 1

    average = total_height / count #calculate average height
    file.close()
    return average

def add_new_data(data): # add new data to file using input
    gender = input("Enter your gender:")
    height = input("Enter your height:")
    weight = input("Enter your weight:")
    bmi = input("Enter your BMI Index:")

    file1 = open(data, 'a', newline='')
    writer = csv.writer(file1)
    writer.writerow([gender, height, weight, bmi]) # add the new data in the csv file directly

    file2 = open(data, 'r', newline='')
    reader = csv.reader(file2)
    
    for row in reader:
        print (row)


result = average_height("labs/lab08/exercise5/bmi.csv")
new_data = add_new_data("labs/lab08/exercise5/bmi.csv")
print (result)
print (new_data)
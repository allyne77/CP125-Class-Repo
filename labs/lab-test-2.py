#allyne syinthia augustine, lab-test-2.py , kelas C02

#Get 5 numbers from user
def process_numbers():
    numbers = []

    for i in range (1,6):
        num = int(input(f"Enter number {i}:"))
        numbers.append(num)

    numbers.sort() #Sort to get numbers in ascending order

    total_sum = sum(numbers) #Calculate sum of all numbers
    largest_number = max(numbers) #Find largest number
    return numbers, total_sum, largest_number

sort_num, total_sum, largest_number = process_numbers() #Call the function

print("Numbers in ascending order:", sort_num)
print("Sum of all numbers:", total_sum)
print("Largest number:", largest_number)

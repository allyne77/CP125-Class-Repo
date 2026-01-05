scores = [85, 92, 78, 88, 95, 73, 91, 87]
print(f"We now have {scores} scores")

# Creating different types of lists
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
prices = [19.99, 24.50, 15.00]

print(fruits)
print(numbers)
print(prices)

# Different data types
integers = [10, 20, 30, 40, 50]
floats = [1.5, 2.3, 3.7, 4.1]
strings = ["apple", "banana", "cherry"]
booleans = [True, False, True, False]

print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", booleans)

fruits = ["apple", "banana", "kiwi", "durian", "guava", "orange"]

print(fruits[0])  # First element
print(fruits[2])  # Third element
print(fruits[5])  # Sixth element

students = [
    ["Ali", 85, 92],
    ["Sara", 90, 88],
    ["Ahmad", 78, 82]
]

# Access the first student's data
print(students[0])  # ['Ali', 85, 92]

# Access Ali's name
print(students[0][0])  # Ali

# Access Sara's second score
print(students[1][2])  # 88

def find_largest_drop(readings):
    largest_drop = []

    for i in range(len(readings) - 1):
        if readings[i] > readings[i + 1]:
            drop = readings[i] - readings[i + 1]
            largest_drop.append(drop)

    if len(largest_drop) == 0:
        return 0.0

    maximum = max(largest_drop)
    return maximum



# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5


def find_bottleneck_index(traceroute):
    max_increase = 0
    bottleneck_index = 0

    for i in range(len(traceroute) - 1):
        hop1 = traceroute[i][1]
        hop2 = traceroute[i + 1][1]

        increase = hop2 - hop1

        if increase > max_increase:
            max_increase = increase
            bottleneck_index = i

    return bottleneck_index

# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1

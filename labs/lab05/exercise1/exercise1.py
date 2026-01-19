
def was_backward_detected(waypoints):
    for i in range (1,len(waypoints)):
        prev_x, prev_y, _ = waypoints[i-1]
        current_x, current_y, _ = waypoints[i]
        if current_x < prev_x or current_y < prev_y:
            return True
        else:
            return False
    


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True

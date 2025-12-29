def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    return current_height * 0.8

def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    return height < 1



def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    height = initial_height
    count = 0
    while height >= 1:
        height = calculate_bounce_height(height)
        count += 1
    return count 


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    height = initial_height
    total_distance = 0
    while height >= 1:
        total_distance += height
        height = calculate_bounce_height(height)
        total_distance += height
    return total_distance

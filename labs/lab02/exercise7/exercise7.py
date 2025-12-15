def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if rect1_right >= rect2_left:
       return True
    elif rect1_left <= rect2_right:
       return True
    elif rect1_bottom >= rect2_top:
       return True
    elif rect1_top <= rect2_bottom:
       return True
    else:
        return False
    


    

    """
    Checks if two rectangles are colliding (overlapping).
    
    Parameters:
    x1, y1: Top-left coordinate of Rectangle 1
    w1, h1: Width and Height of Rectangle 1
    x2, y2: Top-left coordinate of Rectangle 2
    w2, h2: Width and Height of Rectangle 2
    
    Returns:
    True if rectangles overlap, False otherwise
    
    Hint: It's easier to check when they DON'T overlap:
    - Rect 1 is completely to the left of Rect 2
    - Rect 1 is completely to the right of Rect 2
    - Rect 1 is completely above Rect 2
    - Rect 1 is completely below Rect 2
    
    If none of these are true, they must be overlapping!
    """
    # TODO: Implement collision detection logic
    pass

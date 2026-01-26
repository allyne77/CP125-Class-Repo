def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    

    """
    Determines if a year is a leap year according to the Gregorian calendar.
    
    Rules:
    1. If divisible by 4 -> Yes
    2. BUT if divisible by 100 -> No
    3. UNLESS divisible by 400 -> Yes
    
    Parameters:
    year: Integer year value
    
    Returns:
    True if leap year, False otherwise
    """


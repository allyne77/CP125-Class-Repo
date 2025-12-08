# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    total_distance = one_way_km * 2
    total_liters = total_distance / km_per_liter
    cost = total_liters * price_per_liter

    if budget >= cost:
        return True
    else:
        return False
    
# Test your code here
print ("Testing Road Trip Budgeter...")

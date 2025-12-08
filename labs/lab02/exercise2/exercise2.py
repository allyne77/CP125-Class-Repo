# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    food_cost = participants * meal_price
    tent = math.ceil((participants / tent_capacity))
    tent_cost = tent_price * tent
    total_budget = food_cost + tent_cost
    
    return total_budget
    


inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return
    if name in inventory:
        inventory[name] += quantity
        print(f"Item '{name}' already exists. Quantity updated to {inventory[name]}.")
    else:
        inventory[name] = quantity
        print("Item added successfully.")

def delete_item():
    name = input("Enter item name to delete: ")
    if name not in inventory:
        print(f"Error: Item '{name}' not found.")
    else:
        del inventory[name]
        print("Item deleted successfully.")

def search_item():
    name = input("Enter item name to search: ")
    if name not in inventory:
        print(f"Error: Item '{name}' not found.")
    else:
        print(f"Item: {name}, Quantity: {inventory[name]}")

def show_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

def exit_system():
    print("Goodbye! Thank you for using COOPMART Inventory System.")
    return True

# Dictionary mapping choices to functions
menu_options = {
    '1': ('Add item', add_item),
    '2': ('Delete item', delete_item),
    '3': ('Search item', search_item),
    '4': ('Show inventory', show_inventory),
    '5': ('Exit', exit_system),
}

while True:
    print("\n--- COOPMART Inventory Menu ---")
    for key, (label, _) in menu_options.items():
        print(f"{key}. {label}")
    
    choice = input("Enter your choice(1-5): ")
    
    if choice not in menu_options:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")
    else:
        _, func = menu_options[choice]
        result = func()
        if result is True:
            break

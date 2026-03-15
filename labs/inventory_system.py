# Initialize empty inventory dictionary
inventory = {}

# Display menu options
def display_menu():
    print("\n=== INVENTORY SYSTEM ===")
    print("1. Add item")
    print("2. Delete item")
    print("3. Search item")
    print("4. Show inventory")
    print("5. Exit")

# Add new item or update quantity
def add_new_item():
    name = input("Enter item name: ")
    quantity = input("Enter quantity: ")

# Check an item with negative quantity
    quantity = int(quantity)
    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return
        
#Check quantity if it was updated
    if name in inventory:
        inventory[name] += quantity
        print(f"Item '{name}' already exists. Quantity updated to {inventory[name]}.")
    else:
        inventory[name] = quantity
        print(f"Item '{name}' added.")

# Remove item from inventory
def remove_item():
    name = input("Enter item name: ")
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed.")
    else:
        print(f"Error: Item '{name}' not found.")

# Look up item quantity
def find_item():
    name = input("Enter item name: ")
    if name in inventory:
        print(f"Quantity of '{name}': {inventory[name]}")
    else:
        print(f"Error: Item '{name}' not found.")

# Display all inventory items
def list_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}   {quantity}")

# Main loop
while True:
    display_menu()
    user_choice = input("Enter choice (1-5): ")
    
    if user_choice == '1':
        add_new_item()
    elif user_choice == '2':
        remove_item()
    elif user_choice == '3':
        find_item()
    elif user_choice == '4':
        list_inventory()
    elif user_choice == '5':
        print("Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")


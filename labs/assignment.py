def show_menu():
    print("\n=== COOPMART INVENTORY SYSTEM ===")
    print("1. Add item")
    print("2. Delete item")
    print("3. Search item")
    print("4. Show inventory")
    print("5. Exit")


inventory = {}

while True:
    show_menu()
    choice = int(input("Enter choice (1-5): "))

    # Validate menu choice
    if choice < 1 or choice > 5:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")
        continue

    # Exit
    if choice == 5:
        print("Goodbye!")
        break

    # Add item
    elif choice == 1:
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Error: Quantity cannot be negative.")
        else:
            if item in inventory:
                inventory[item] += quantity
                print(f"Item '{item}' already exists. Quantity updated to {inventory[item]}.")
            else:
                inventory[item] = quantity
                print(f"Item '{item}' added.")

    # Delete item
    elif choice == 2:
        item = input("Enter item name: ")

        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            del inventory[item]
            print(f"Item '{item}' removed.")

    # Search item
    elif choice == 3:
        item = input("Enter item name: ")

        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            print(f"Quantity of '{item}': {inventory[item]}")

    # Show inventory
    elif choice == 4:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item, quantity in inventory.items():
                print(f"{item}   {quantity}")

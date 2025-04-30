inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 8
}

def show_inventory():
    print("\nCurrent inventory:")
    for fruit, quantity in inventory.items():
        print(f"{fruit.title()}: {quantity}")
    print()

def add_product():
    fruit = input("Enter fruit name to add: ").lower()
    quantity = int(input("Enter quantity: "))
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    print(f"{fruit.title()} added/updated successfully!\n")

def remove_product():
    fruit = input("Enter fruit name to remove: ").lower()
    if fruit in inventory:
        del inventory[fruit]
        print(f"{fruit.title()} removed from inventory.\n")
    else:
        print("Fruit not found in inventory.\n")

def low_stock(threshold=5):
    print(f"\nFruits with stock less than {threshold}:")
    for fruit, quantity in inventory.items():
        if quantity < threshold:
            print(f"{fruit.title()}: {quantity}")
    print()

def main():
    while True:
        print("Choose an action:")
        print("1 - Show products")
        print("2 - Add product")
        print("3 - Remove product")
        print("4 - Show products with low stock")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            low_stock()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
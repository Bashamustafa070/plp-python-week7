# shopping_list.py

# 1. Start with an empty list
shopping_list = []

# 2. Use a loop to show a small menu again and again
while True:
    choice = input("\nOptions - add / remove / show / done: ").strip().lower()
    
    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added.")
    
    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        # Check it is actually in the list with 'in' before removing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your list is empty.")
        else:
            for item in shopping_list:
                print(item)
                
    elif choice == "done":
        print("Goodbye! Have a great day.")
        break
        
    else:
        print("Invalid option. Please choose add, remove, show, or done.")
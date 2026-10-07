print("Hello from main")
def menu():
    print("*******Menu*******")
    print("1. Enter 1 for New Diary")
    print("2. Enter 2 for View/ modify Existing Diary")
    print("3. Enter 3 for Delete Diary")
    print("4. Exit")
    choice = input("Select an option: ")
    return choice

def submenu():
    print("*******Sub Menu*******")
    print("1. Enter 1 for New Entry")
    print("2. Enter 2 for Delete Entry")
    print("3. Enter 3 for Filter and view Entries")
    print("4. Back to Main Menu1")
    choice = input("Select an option: ")
    return choice



choice = menu()
if choice == "1":
    print("New Diary selected")
elif choice == "2":
    print("View/modify Existing Diary selected")
    submenu_choice = submenu()
elif choice == "3":
    print("Delete Diary selected")
elif choice == "4":
    print("Exiting...")
else:
    print("Invalid option selected")
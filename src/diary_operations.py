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

def create_new_diary():
    diary_name = input("Enter the name of the new diary: ")
    diary_name = diary_name.replace(" ", "_")

    try:
        with open(diary_name+".txt", "x"):
            pass

        print("New Diary created successfully.")
        return diary_name

    except FileExistsError:
        print("A diary with that name already exists.")
        return None

def delete_diary():
    diary_name = input("Enter the name of the diary to delete: ")
    diary_name = diary_name.replace(" ", "_")

    try:
        import os
        os.remove(diary_name+".txt")
        print("Diary deleted successfully.")
    except FileNotFoundError:
        print("Diary not found.")

def view_modify_diary():
    diary_name = input("Enter the name of the diary to open: ")
    diary_name = diary_name.replace(" ", "_")

    try:
        with open(diary_name + ".txt", "r"):
            pass

        print("Diary opened successfully.")
        submenu()
        return diary_name

    except FileNotFoundError:
        print("Diary not found.")
        return None
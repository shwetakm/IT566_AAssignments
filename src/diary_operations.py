# menu and submenu for the diary application starts
def menu():
    print("\n*******Menu*******\n")
    print("1: New Diary | 2: View/Modify Existing Diary | 3: Delete Diary | 4: Exit\n")
    choice = input("Enter an option: ")
    return choice

def submenu():
    print("\n*******Sub Menu*******\n")
    print("1: Insert New | 2: Modify Existing Entry | 3: Delete Entry | 4: Filter by Date | 5: Back to Main Menu\n")
    choice = input("Enter an option: ")
    return choice
# menu and submenu functions for the diary application ends

# menu functions for the diary application starts
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

def select_diary():
    diary_name = input("Enter the name of the diary to open: ")
    diary_name = diary_name.replace(" ", "_")

    try:
        with open(diary_name + ".txt", "r") as diary:
            view_diary(diary)
        choice = submenu()

        if choice == "1":
            print("insert new entry")
            insert_new_entry(diary_name)
        elif choice == "2":
            print("modify existing entry")
            modify_entry(diary_name)
        elif choice == "3":
            print("Delete an entry")
            delete_entry(diary_name)
        elif choice == "4":
            print("Filter by date")
            filter_by_date(diary_name)
        elif choice == "5":
            print("Returning back to main menu...")
            menu()
        else:
            print("Invalid option selected")

        if(choice == "1" or choice == "2" or choice == "3"):
         with open(diary_name + ".txt", "r") as diary:
                     view_diary(diary)
        return diary_name

    except FileNotFoundError:
        print("Diary not found.")
        return None

# menu functions for the diary application ends

# submenu functions for the diary application starts
def view_diary(diary):
    string_entries = diary.readlines()
    print("----------------------------------------------------------------------------------------")
    for i, line in enumerate(string_entries, 1):
        print(f"{i}. {line.strip()}")
    print("----------------------------------------------------------------------------------------")

def insert_new_entry(diary_name):
    entry = input("Enter the new entry: format (YYYY-MM-DD text) ")
    try:
        with open(diary_name + ".txt", "a") as diary:
            diary.write(entry + "\n")
        print("Entry inserted successfully.")
    except FileNotFoundError:
        print("Diary not found.")

def delete_entry(diary_name):
    entry_number = int(input("Enter the entry number to delete: "))
    try:
        with open(diary_name + ".txt", "r") as diary:
            lines = diary.readlines()
        if 1 <= entry_number <= len(lines):
            del lines[entry_number - 1]
            with open(diary_name + ".txt", "w") as diary:
                diary.writelines(lines)
            print("Entry deleted successfully.")
        else:
            print("Invalid entry number.")
    except FileNotFoundError:
        print("Diary not found.")

def modify_entry(diary_name):
    entry_number = int(input("Enter the entry number to modify: "))
    try:
        with open(diary_name + ".txt", "r") as diary:
            lines = diary.readlines()
        if 1 <= entry_number <= len(lines):
            new_entry = input("Enter the new entry: ")
            lines[entry_number - 1] = new_entry + "\n"
            with open(diary_name + ".txt", "w") as diary:
                diary.writelines(lines)
            print("Entry modified successfully.")
        else:
            print("Invalid entry number.")
    except FileNotFoundError:
        print("Diary not found.")

def filter_by_date(diary_name):
    date = input("Enter the date to filter entries (YYYY-MM-DD): ")
    try:
        with open(diary_name + ".txt", "r") as diary:
            lines = diary.readlines()
            filtered_lines = [line for line in lines if date in line]
        if filtered_lines:
            print("Filtered entries:")
            for i, line in enumerate(filtered_lines, 1):
                    print(f"{i}. {line.strip()}")
        else:
                print("No entries found for the specified date.")
    except FileNotFoundError:
            print("Diary not found.")


# submenu functions for the diary application ends
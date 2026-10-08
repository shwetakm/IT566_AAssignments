from diary_operations import menu, create_new_diary, select_diary, delete_diary

print("Diary Application")

choice = menu()
if choice == "1":
    print("New Diary selected")
    create_new_diary()
elif choice == "2":
    print("Select Existing Diary selected")
    select_diary()
elif choice == "3":
    print("Delete Diary selected")
    delete_diary()
elif choice == "4":
    print("Exiting...")
else:
    print("Invalid option selected")
import actions

def show_menu():
    while True:
        print("=== Student Control System ===")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Show Top 3 Students")
        print("6. Show Average of All Students")
        print("7. Export All Data to CSV")
        print("8. Import Data from CSV")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            actions.add_student()
        elif choice == '2':
            actions.show_students()
        elif choice == '3':
            actions.save_data()
        elif choice == '4':
            actions.load_data()
        elif choice == '5':
            actions.show_top_students()
        elif choice == '6':
            actions.show_individual_averages()
        elif choice == '7':
            actions.export_csv()
        elif choice == '8':
            actions.import_csv()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")
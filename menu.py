import actions
from data import export_csv, import_csv

def show_menu():
    students = []  # local variable fix requested 

    while True: # here also deleted the options that were doing the same 
        print("=== Student Control System ===")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Show Top 3 Students")
        print("4. Show Overall Average")
        print("5. Export Data to CSV")
        print("6. Import Data from CSV")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            students = actions.add_student(students)
        elif choice == '2':
            actions.show_students(students)
        elif choice == '3':
            actions.show_top_students(students)
        elif choice == '4':
            actions.show_overall_average(students)
        elif choice == '5':
            export_csv(students)
        elif choice == '6':
            students = import_csv()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

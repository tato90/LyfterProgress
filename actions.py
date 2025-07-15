import data

# Lista global para guardar todos los estudiantes
students = []

def ask_for_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except:
            print("Please enter a valid number.")

def add_student():
    full_name = input("Full Name: ")
    section = input("Section (e.g., 11B): ")
    grade1 = ask_for_grade("Spanish Grade (0-100): ")
    grade2 = ask_for_grade("English Grade (0-100): ")
    grade3 = ask_for_grade("Social Studies Grade (0-100): ")
    grade4 = ask_for_grade("Science Grade (0-100): ")

    student = {
        'full_name': full_name,
        'section': section,
        'grades': {
            'Spanish': grade1,
            'English': grade2,
            'Social Studies': grade3,
            'Science': grade4
        }
    }

    students.append(student)
    print("Student added.\n")

def show_students():
    if not students:
        print("No students registered.\n")
        return
    for i, s in enumerate(students):
        print(f"{i+1}. {s['full_name']} - Section: {s['section']}")
        for subject, grade in s['grades'].items():
            print(f"  {subject}: {grade}")
        total = sum(s['grades'].values())
        average = total / 4
        print(f"  Average: {average:.2f}\n")

def save_data():
    data.export_csv(students)

def load_data():
    global students
    students = data.import_csv()

def show_top_students():
    if not students:
        print("No students registered.\n")
        return
    students_avg = []
    for s in students:
        total = sum(s['grades'].values())
        avg = total / 4
        students_avg.append((s, avg))
    # Ordena promedios
    students_avg.sort(key=lambda x: x[1], reverse=True)

    print("Top 3 students:\n")
    for i in range(min(3, len(students_avg))):
        s, avg = students_avg[i]
        print(f"{i+1}. {s['full_name']} - Average: {avg:.2f}")
        print(f"   Section: {s['section']}")
        for subject, grade in s['grades'].items():
            print(f"     {subject}: {grade}")
        print()

def show_individual_averages():
    if not students:
        print("No students registered.\n")
        return
    for s in students:
        total = sum(s['grades'].values())
        average = total / len(s['grades'])
        print(f"{s['full_name']}: {average:.2f}")

# Funciones para exportar/importar CSV
def export_csv():
    data.export_csv(students)

def import_csv():
    global students
    students = data.import_csv()
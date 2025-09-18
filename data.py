import csv
import os

def export_csv(students, filename='students.csv'):
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['full_name', 'section', 'Spanish', 'English', 'Social Studies', 'Science']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    'full_name': s['full_name'],
                    'section': s['section'],
                    'Spanish': s['grades']['Spanish'],
                    'English': s['grades']['English'],
                    'Social Studies': s['grades']['Social Studies'],
                    'Science': s['grades']['Science']
                })
        print("Data exported to CSV successfully.")
    except:
        print("Error exporting to CSV.")

def import_csv(filename='students.csv'):
    if not os.path.exists(filename):
        print("No CSV file found.")
        return []

    students_list = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = {
                    'full_name': row['full_name'],
                    'section': row['section'],
                    'grades': {
                        'Spanish': float(row['Spanish']),
                        'English': float(row['English']),
                        'Social Studies': float(row['Social Studies']),
                        'Science': float(row['Science'])
                    }
                }
                students_list.append(student)
        print("Data imported from CSV.")
        return students_list
    except:
        print("Error importing CSV.")
        return []

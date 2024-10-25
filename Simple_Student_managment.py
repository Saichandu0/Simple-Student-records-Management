# Dictionary to store students' information
student_directory = {
    1001: {"name": "John Doe", "grade": 10},
    1002: {"name": "Jane Smith", "grade": 11},
    1003: {"name": "Emily Johnson", "grade": 9},
    1004: {"name": "Rajesh", "grade": 12},
    1005: {"name": "Suresh", "grade": 10},
    1006: {"name": "Emily Johnson", "grade": 9},
    1007: {"name": "Mike Johnson", "grade": 9},
    1008: {"name": "Leena Joe", "grade": 10},
    1009: {"name": "Leo Johnson", "grade": 11}
}

# Function to display all students
def view_students():
    if student_directory:
        print("\n--- Student Directory ---")
        for student_id, info in student_directory.items():
            print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")
    else:
        print("No students found.")

# Function to add a new student
def add_student():
    name = input("Enter the student's name: ").strip()
    while True:
        grade = input("Enter the student's grade (9-12): ").strip()
        if grade.isdigit() and 9 <= int(grade) <= 12:
            grade = int(grade)
            break
        else:
            print("Invalid grade. Please enter a valid grade (9-12).")
    
    # Generate a unique student ID
    new_id = max(student_directory.keys()) + 1 if student_directory else 1001
    student_directory[new_id] = {"name": name, "grade": grade}
    print(f"Student '{name}' added with ID: {new_id}, Grade: {grade}")

# Function to update a student's grade
def update_grade():
    student_id = input("Enter the student ID to update grade: ").strip()
    if student_id.isdigit() and int(student_id) in student_directory:
        student_id = int(student_id)
        new_grade = input(f"Enter the new grade for {student_directory[student_id]['name']}: ").strip()
        if new_grade.isdigit() and 9 <= int(new_grade) <= 12:
            student_directory[student_id]['grade'] = int(new_grade)
            print(f"Grade for student '{student_directory[student_id]['name']}' updated to {new_grade}")
        else:
            print("Invalid grade entered.")
    else:
        print("Student ID not found.")

# Function to delete a student
def delete_student():
    student_id = input("Enter the student ID to delete: ").strip()
    if student_id.isdigit() and int(student_id) in student_directory:
        student_id = int(student_id)
        print(f"Student Name: {student_directory[student_id]['name']}, Grade: {student_directory[student_id]['grade']}")
        confirmation = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            del student_directory[student_id]
            print("Student deleted.")
        else:
            print("Student deletion canceled.")
    else:
        print("Student ID not found.")

# Function to display the main menu
def main_menu():
    print("Welcome to the Student Management System!")
    while True:
        print("\n--- Menu ---")
        print("1. View All Students")
        print("2. Add a New Student")
        print("3. Update a Student's Grade")
        print("4. Delete a Student Record")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            view_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_grade()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Thank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to run the program
def main():
    main_menu()

if __name__ == "__main__":
    main()


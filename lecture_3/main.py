from typing import List, Dict, Optional

StudentDict = Dict[str, List[int] | str]
StudentList = List[StudentDict]

students: StudentList = []


def output_menu_text() -> None:
    """Display the main menu options."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate report for all students")
    print("4. Find the top student")
    print("5. Exit program")


def find_student_by_name(name: str) -> Optional[StudentDict]:
    """
    Find a student by name (case-insensitive).
    """
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def student_exists(name: str) -> bool:
    """
    Check if a student already exists
    """
    return find_student_by_name(name) is not None


def add_new_student() -> None:
    """Add a new student to the system"""
    while True:
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty! Please try again")
            continue

        if student_exists(name):
            print("Student already exists! Please try a different name")
            continue

        students.append({"name": name, "grades": []})
        break


def is_valid_grade(grade: int) -> bool:
    """
    Check if grade is within valid range.
    """
    return 0 <= grade <= 100


def add_grades() -> None:
    """Add grades for a specific student."""
    while True:
        name = input("Enter student name: ").strip()
        student = find_student_by_name(name)

        if not student:
            print(f"Student '{name}' not found! Please try again")
            continue

        break

    print(f"Adding grades for {student['name']}.")

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()

        if grade_input == "done":
            break

        try:
            grade = int(grade_input)
            if is_valid_grade(grade):
                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100! Please try again")
        except ValueError:
            print("Invalid input. Please enter a number")


def calculate_average(grades: List[int]) -> float:
    """
    Calculate average of grades, handling empty list
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def generate_report() -> None:
    """Generate report of all students with statistics"""
    if not students:
        print("No students available!")
        return

    print("\n--- Student Report ---")
    averages = []

    for student in students:
        grades = student["grades"]

        if grades:
            average = calculate_average(grades)
            averages.append(average)
            print(f"{student['name']}'s average grade is {average:.1f}")
        else:
            print(f"{student['name']}'s average grade is N/A")

    if averages:
        print(f"\nMax Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages) / len(averages):.1f}")
    else:
        print("\nNo grades available for statistics")


def switch(choice: int) -> bool:
    """
    Handle menu choice selection.
    """
    if choice == 1:
        add_new_student()
    elif choice == 2:
        add_grades()
    elif choice == 3:
        generate_report()
    elif choice == 4:
        print("4. Find the top student")
    elif choice == 5:
        print("Exiting program.")
        return True
    else:
        print("Invalid choice! Please select 1-5.")
    return False


def main() -> None:
    """Main program loop."""
    print("Welcome to Student Grade Analyzer!")

    while True:
        output_menu_text()
        try:
            choice = int(input("Enter your choice: "))
            should_exit = switch(choice)
            if should_exit:
                break
        except ValueError:
            print("Please input a valid number (1-5)!")


if __name__ == "__main__":
    main()

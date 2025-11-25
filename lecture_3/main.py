from typing import List, Dict

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


def switch(choice: int) -> bool:
    """
    Handle menu choice selection.
    """
    if choice == 1:
        print("1. Add a new student")
    elif choice == 2:
        print("2. Add grades for a student")
    elif choice == 3:
        print("3. Generate report for all students")
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

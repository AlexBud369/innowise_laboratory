import os
import sqlite3


def verify_database():
    """Verify school.db is correct."""
    print("🔍 Verifying school.db database...")

    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # 1. Check tables exist
        cursor.execute(
            """
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
        """
        )
        tables = [row[0] for row in cursor.fetchall()]

        expected_tables = ["students", "grades"]
        if set(tables) == set(expected_tables):
            print(f"Tables: {tables}")
        else:
            print(f"Tables mismatch. Found: {tables}, Expected: {expected_tables}")
            return False

        # 2. Check student count
        cursor.execute("SELECT COUNT(*) FROM students")
        student_count = cursor.fetchone()[0]
        if student_count == 9:
            print(f"Students: {student_count}/9")
        else:
            print(f"Wrong student count: {student_count}, Expected: 9")
            return False

        # 3. Check grade count
        cursor.execute("SELECT COUNT(*) FROM grades")
        grade_count = cursor.fetchone()[0]
        if grade_count == 26:
            print(f"Grades: {grade_count}/26")
        else:
            print(f"Wrong grade count: {grade_count}, Expected: 26")
            return False

        # 4. Check specific data points
        cursor.execute("SELECT full_name FROM students WHERE id = 1")
        student_1 = cursor.fetchone()[0]
        if student_1 == "Alice Johnson":
            print(f"First student: {student_1}")
        else:
            print(f"Wrong first student: {student_1}")
            return False

        # 5. Run Query 3 to verify data
        cursor.execute(
            """
            SELECT g.subject, g.grade 
            FROM grades g
            JOIN students s ON g.student_id = s.id
            WHERE s.full_name = 'Alice Johnson'
            ORDER BY g.subject
        """
        )
        alice_grades = cursor.fetchall()
        expected_grades = [("English", 92), ("Math", 88), ("Science", 85)]

        if alice_grades == expected_grades:
            print(f"Alice's grades: {alice_grades}")
        else:
            print(f"Alice's grades mismatch: {alice_grades}")
            return False

        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False


def verify_queries_file():
    """Verify queries.sql is complete"""
    print("\nVerifying queries.sql file...")

    try:
        with open("queries.sql", "r", encoding="utf-8") as f:
            content = f.read()

        # Check all required queries are present
        required_sections = [
            "CREATE TABLE students",
            "CREATE TABLE grades",
            "INSERT INTO students",
            "INSERT INTO grades",
            "Alice Johnson",
            "AVG(g.grade)",
            "birth_year > 2004",
            "GROUP BY subject",
            "LIMIT 3",
            "grade < 80",
        ]

        missing = []
        for section in required_sections:
            if section not in content:
                missing.append(section)

        if not missing:
            print("All required queries found")
            return True
        else:
            print(f"Missing in queries.sql: {missing}")
            return False

    except IOError as e:
        print(f"Cannot read queries.sql: {e}")
        return False


def verify_file_sizes():
    """Check files exist and have reasonable sizes."""
    print("\nVerifying file sizes...")

    files_to_check = [
        ("school.db", 5000, 100000),  # Should be between 5KB and 100KB
        ("queries.sql", 1000, 10000),  # Should be between 1KB and 10KB
    ]

    for filename, min_size, max_size in files_to_check:
        if not os.path.exists(filename):
            print(f"{filename} does not exist!")
            return False

        size = os.path.getsize(filename)
        if min_size <= size <= max_size:
            print(f"{filename}: {size} bytes (reasonable size)")
        else:
            print(f"{filename}: {size} bytes (unexpected size)")
            # Don't fail for size, just warn

    return True


def main():
    """Run complete verification."""
    print(" checking database...")

    all_ok = True

    # Step 1: Check files exist
    print("\nStep 1: Checking files exist...")
    for file in ["school.db", "queries.sql"]:
        if os.path.exists(file):
            print(f"   {file}")
        else:
            print(f"   {file} - MISSING!")
            all_ok = False

    if not all_ok:
        print("\nCannot proceed - missing files!")
        return

    # Step 2: Verify database
    if not verify_database():
        all_ok = False

    # Step 3: Verify queries file
    if not verify_queries_file():
        all_ok = False

    # Step 4: Check file sizes
    verify_file_sizes()

    if all_ok:
        print("Task is correct")
        print("   You can submit these files:")
        print("   - lecture_4/school.db")
        print("   - lecture_4/queries.sql")
    else:
        print("FAILURE: Some checks failed.")


if __name__ == "__main__":
    main()

import json

try:
    with open("students.json", "r") as file:
         students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add Student Scores")
    print("2. View Results")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option:")

    if choice == "1":
        name = input("Enter student name: ")

        if name == "":
            print("Name can not be empty.")
            continue

        if any(s["name"].lower() == name.lower() for s in students):
            print("Student already exists.")
            continue

        scores = input("Enter scores separated by space: ").split()

        try:
            scores = [int(score) for score in scores]
        except ValueError:
            print("Score must be numbers only.")
            continue

        if len(scores) == 0:
            print("You must enter at least one score.")
            continue

        average = sum(scores) / len(scores)

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        students.append({
            "name": name,
            "scores": scores,
            "average": average,
            "grade": grade
        })

        with open("students.json", "w") as file:
            json.dump(students, file)

        print("Student added!")

    elif choice == "2":
        print("\n--- Results ---")
        if not students:
            print("No student records yet.")
            continue
        for student in students:
            print(f"{student['name']} - Avg: {student['average']:.2f}, Grade: {student['grade']}")

        averages = [student["average"] for student in students]
        class_avg = sum(averages) / len(averages)
        highest = max(averages)
        lowest = min(averages)

        print("\n ---Class Statistics ---")
        print(f"Total Students:{len(students)}")
        print(f"Class Average: {class_avg:.2f}")
        print(f"Highest Average: {highest:.2f}")
        print(f"Lowest Average: {lowest:.2f}")

    elif choice == "3":
        search_name = input("Enter student name to search: ").strip()

        found = False
        for student in students:
            if student["name"].lower() == search_name.lower():
                print(f"\nFound: {student['name']} - Avg: {student['average']:.2f}, Grade: {student['grade']}")
                found = True
                break
        if not found:
            print("Student not found")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].strip().lower() == delete_name.lower():
                  students.remove(student)
                  found = True
                  break
        
        if found:
            with open("students.json", "w") as file:
                json.dump(students, file)
            print("Student deleted successfully.")
        else:
            print("Student not found.")


    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")
        
        
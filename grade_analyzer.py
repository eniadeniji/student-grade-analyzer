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
    print("3. Exit")

    choice = input("Choose an option:")

    if choice == "1":
        name = input("Enter student name: ")

        if name == "":
            print("Name can not be empty.")
            continue

        scores = input("Enter scores separated by space: ").split()

        try:
            scores = [int(score) for score in scores]
        except ValueError:
            print("Score must be numbers only.")
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
            print(f"{student['name']} → Avg: {student['average']:.2f}, Grade: {student['grade']}")

    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")
        
        
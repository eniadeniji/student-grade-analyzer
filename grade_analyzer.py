"""
Student Grade Analyzer (CLI)

Features:
- Add student scores
- Automatic grade calculation
- Search student
- Delete student
- Class Statistics
- JSON persistence

Technologies:
- Python
- JSON
- CLI
- File I/O
"""

import json

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def add_student(students):
    name = input("Enter student name: ")

    if name == "":
            print("Name can not be empty.")
            return students

    if any(s["name"].lower() == name.lower() for s in students):
            print("Student already exists.")
            return students

    scores = input("Enter scores separated by space: ").split()

    try:
            scores = [int(score) for score in scores]
    except ValueError:
        print("Score must be numbers only.")
        return students

    if len(scores) == 0:
        print("You must enter at least one score.")
        return students

    average = sum(scores) / len(scores)

    grade = calculate_grade(average)

    students.append({
            "name": name,
            "scores": scores,
            "average": average,
            "grade": grade
        })

    save_students(students)

    print("Student added!")
    return students

def view_results(students):
    print("\n--- Results ---")
    if not students:
            print("No student records yet.")
            return
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

def search_student(students):
    search_name = input("Enter student name to search: ").strip()

    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"\nFound: {student['name']} - Avg: {student['average']:.2f}, Grade: {student['grade']}")
            found = True
            break
    if not found:
            print("Student not found")

def calculate_grade(average):
     if average >= 70:
            return  "A"
     elif average >= 60:
            return  "B"
     elif average >= 50:
            return  "C"
     elif average >= 40:
            return  "D"
     else:
            return "F"
     
def save_students(students):
     with open(FILE_NAME, "w") as file:
          json.dump(students, file, indent=4)

def delete_student(students):
     delete_name = input("Enter student name to delete: ").strip()

     for student in students:
          if student["name"].lower() == delete_name.lower():
              students.remove(student)
              save_students(students)
              print("Student deleted successfully")
              return students
     print("Student not found.")
     return students
     
def main():
    students = load_students()

    while True:
         print("\n--- Student Grade Analyzer ---")
         print("1. Add Student Scores")
         print("2. View Results")
         print("3. Search Student")
         print("4. Delete Student")
         print("5. Exit")

         choice = input("Choose an option: ")

         if choice == "1":
           students = add_student(students)

         elif choice == "2":
          view_results(students)

         elif choice == "3":
          search_student(students)

         elif choice == "4":
          students = delete_student(students)
        
         elif choice == "5":
          print("Goodbye!")
          break
    
         else:
          print("Invalid choice.")

if __name__ == "__main__":
     main()
        
        
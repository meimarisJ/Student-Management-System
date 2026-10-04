import json
from src.processing import analyze_students, get_students, add_student, remove_student

students = None

try:
    with open("Json/students.json", "r") as file:
        students  = json.load(file)
except FileNotFoundError:
    print("File not found.")

options = [
    "Show Students",
    "Add Students",
    "Remove Students",
    "Filter Students",
    "Analyze Students",
    "Exit"
]



if students is not None:
    
    while True :
        print("\n===== Student Management =====")
        for number , option in enumerate(options, start=1):
            print(f"{number}. {option}")
        choice = int(input("\nChoose an option.\n"))
        if choice == 1: # Show all Students
            
            for number, student in enumerate (students, start=1):
                print(f"{number}. {student}")
            print()

            
        elif choice == 2: # Add Student
            
            result =add_student(students)
            with open("Json/students.json","w") as file:
                json.dump(students,file, indent= 4)   
        elif choice == 3: #Remove Students
            
            remove_student(students , input("Enter the name of the student to remove: "))
            with open("Json/students.json","w") as file:
                    json.dump(students,file, indent= 4) 
        elif choice == 4: #Filter Students with min age, min grade
            
            min_grade = int(input("Enter minimum grade: "))
            min_age = int(input("Enter minimum age: "))
            result = get_students(students,min_grade,min_age)
            print()

            if not result:
                print("No student found with that criteria.\n")
            else:
                for number , student in enumerate (result, start=1):
                    print(f"{number}. {student}")
                print()
                with open("Json/filtered_students.json", "w") as file:
                    json.dump(result,file, indent = 4)
                    
        elif choice == 5 : # Show avg grade , max grade, min grade , number of students that passed (grade >= 10) and best student based on grade.
            result = analyze_students(students)
            if result is None:
                print("No students to analyze.\n")
            else:
                for key, value in result.items():
                    print(f"{key}: {value}")
                print()
        elif choice == 6: # Exit Program
            
            print("\nExiting program.")
            break
        else:
            print("Wrong input.Try again.\n")

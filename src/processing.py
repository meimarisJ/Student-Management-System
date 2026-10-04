def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def add_student(students):
    name = input("Name: ")
    while not name.strip():
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Name: ")
    age = read_int("Age: ")
    while age < 0:
        print("Age cannot be negative. Please enter a valid age.")
        age = read_int("Age: ")
    grade = read_int("Grade: ")
    while grade < 0 or grade > 20:
        print("Grade must be between 0 and 20. Please enter a valid grade.")
        grade = read_int("Grade: ")
    new_student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(new_student)
    print("Student added.\n")
    

def remove_student(students, name):
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print()
            print("Student removed.\n")
            found = True
            break
                
        
    if not found:
        print()
        print("Student not found.")
        print()
def analyze_students(students):
    if not students:
        return None
    total_grade = 0
    passed = 0
    highest_grade = students[0]["grade"]
    lowest_grade = students[0]["grade"]
    best_student = students[0]["name"]
    for student in students:
        total_grade+= student["grade"]
        if student["grade"] > highest_grade:
            highest_grade = student["grade"]
            best_student = student["name"]
        if lowest_grade > student["grade"]:
            lowest_grade = student["grade"]    
        if student["grade"] >= 10:
            passed += 1 
    average_grade = total_grade / len(students)
    return {
        "average grade": average_grade,
        "highest grade": highest_grade,
        "lowest grade": lowest_grade,
        "passed": passed,
        "best student": best_student
    }


def get_students(students, minimum_grade, minimum_age):
    result = []
    for student in students:
        if (student["grade"]>= minimum_grade) and (student["age"] >= minimum_age):
            result.append(student)

    return result
students = [
    {"id": 101, "name": "Ravi", "marks": 85},
    {"id": 102, "name": "Anil", "marks": 72},
    {"id": 103, "name": "Kiran", "marks": 91},
    {"id": 104, "name": "Priya", "marks": 78}
]

def add_student(student_id, name, marks):       # 1. Add a new student
    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        return
    for student in students:
        if student["id"] == student_id:
            print("ID already exists")
            return
    students.append({
        "id": student_id,
        "name": name,
        "marks": marks
    })
    print("Student added successfully")

def search_student(student_id):  # 2. Search student by ID
    for student in students:
        if student["id"] == student_id:
            print(student)
            return
    print("Student not found")

def update_marks(student_id, marks):        # 3. Update student's marks
    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        return
    for student in students:
        if student["id"] == student_id:
            student["marks"] = marks
            print("Marks updated successfully")
            return
    print("Student not found")

def delete_student(student_id):     # 4. Delete student by ID
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully")
            return
    print("Student not found")

def display_students():         # 5. Display all students
    for student in students:
        print(student)

def highest_marks():        # 6. Find student with highest marks
    if len(students) == 0:
        print("No students available")
        return
    highest = students[0]
    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student
    print("Highest marks:", highest)

add_student(105, "Arjun", 88)

search_student(103)

update_marks(102, 90)

delete_student(104)

display_students()

highest_marks()


#
student = {
    "id": 101,
    "name": "Ravi",
    "marks": 80
}
def update_marks(student, marks):

    if marks >= 0 and marks <= 100:
        student["marks"] = marks
        return True

    return False

update_marks(student, 95)

print(student["marks"])
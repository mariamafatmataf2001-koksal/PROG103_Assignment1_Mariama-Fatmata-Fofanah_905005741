student = []

num = int(input("Enter the number of students: "))

for i in range(num):
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    score = int(input("Enter student score: "))

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    student.append((name, student_id, score, grade))

print("\nStudent Records:")
for s in student:
    print("Name:",s[0], "ID:",s[1], "Score:",s[2], "Grade:",s[3])

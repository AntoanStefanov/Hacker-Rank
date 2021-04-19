n = int(input())

students = []
lowest_grade = 100000000000
for student in range(n):
    name = input()
    grade = float(input())
    if grade < lowest_grade:
        lowest_grade = grade
    students.append([name, grade])

students = [student for student in students if student[1] > lowest_grade]

min_student = min(students, key=lambda x: x[1])
min_grade = min_student[1]
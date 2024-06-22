

n = int(input())

students = {}

for _ in range(n):
    name, *marks = input().split()
    students[name] = list(map(float, marks))

student_name = input()
student_marks = students[student_name]

average = sum(student_marks) / len(student_marks)
print(f'{average:.2f}')
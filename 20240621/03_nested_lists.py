

n = int(input())
students = [[input(), float(input())] for _ in range(n)]

second_lowest = sorted(set([grade for name, grade in students]))[1]
for name, grade in sorted(students):
    if grade == second_lowest:
        print(name)

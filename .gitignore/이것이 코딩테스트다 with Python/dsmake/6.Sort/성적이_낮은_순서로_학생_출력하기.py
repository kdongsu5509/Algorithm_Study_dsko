n = int(input())

students = []

for _ in range(n):
    name, grade = input().split()
    students.append((name, grade))

#파이썬 내장 라이브러리 or 퀵 정렬 사용하면 될 것 같음.

sorted_student = sorted(students, key=lambda student: student[1])

for a in range(n):
    print(sorted_student[a][0], end=" ")
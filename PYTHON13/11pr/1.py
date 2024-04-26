num_grades = int(input("Введите количество оценок: "))

grades = []

print("Введите оценки:")
for i in range(num_grades):
    grade = float(input())
    grades.append(grade)

print("Введенные оценки:")
for grade in grades:
    print(grade)

average_grade = sum(grades) / num_grades
print("Средняя оценка за урок:", average_grade)
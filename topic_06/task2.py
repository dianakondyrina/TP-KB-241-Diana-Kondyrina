students = [
    {"name": "Emma", "grade": 8},
    {"name": "Bob",  "grade": 65},
    {"name": "Zak",  "grade": 12},
    {"name": "Jon",  "grade": 44}
]

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за ім'ям:")
for s in sorted_by_name:
    print(s)

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("\nСортування за оцінкою:")
for s in sorted_by_grade:
    print(s)
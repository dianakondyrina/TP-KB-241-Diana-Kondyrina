class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years"

students = [
    Student("Bob", 32),
    Student("Emma", 12),
    Student("Jon", 9),
    Student("Zak", 50)
]

def main():
    sort_name = sorted(students, key=lambda student: student.name)
    
    print("\nSorted by name: ")
    for student in sort_name:
        print(student)
        
    sort_age = sorted(students, key=lambda student: student.age)
    
    print("\nSorted by age: ")
    for student in sort_age:
        print(student)
    
main()
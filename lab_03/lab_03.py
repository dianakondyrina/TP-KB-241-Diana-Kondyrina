import sys
from student import Student
from student_list import StudentList
from file import FileManager

def main():
    filename = "students.csv"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file_manager = FileManager(filename)
    student_list = StudentList()

    file_manager.load(student_list)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")

        match choice.lower():
            case "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                address = input("Please enter student address: ")
                date = input("Please enter student date: ")

                new_student = Student(name, phone, address, date)
                student_list.addNewStudent(new_student)
                print("Student added")

            case "u":
                name = input("Enter name to update: ")
                student = student_list.findStudent(name)

                if student:
                    print(f"Current data: {student}")
                    new_name = input("New name: ") or student.name
                    new_phone = input("New phone: ") or student.phone
                    new_address = input("New address: ") or student.address
                    new_date = input("New date: ") or student.date

                    updated = Student(new_name, new_phone, new_address, new_date)
                    student_list.updateStudent(name, updated)
                    print("Updated")
                else:
                    print("Student not found")

            case "d":
                name = input("Enter name to delete: ")
                if student_list.deleteStudent(name):
                    print("Deleted")
                else:
                    print("Student not found")

            case "p":
                student_list.print_all()

            case "x":
                file_manager.save(student_list.getAll())
                print("Exit")
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
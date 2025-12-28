from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def getAll(self):
        return self.students
    
    def addNewStudent(self, student: Student):
        insertPosition = 0
        for item in self.students:
            if student.name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
    
    def deleteStudent(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False

    def findStudent(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def updateStudent(self, old_name, new_student):
        actual_student = self.findStudent(old_name)
        
        if actual_student is not None:
            self.deleteStudent(old_name)
            self.addNewStudent(new_student)
            return True 
        else:
            print("Student not found")
            return False
    
    def print_all(self):
        if not self.students:
            print("List is empty")
            return
        for s in self.students:
            print(s)
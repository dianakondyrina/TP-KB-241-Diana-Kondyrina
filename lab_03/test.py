from student import Student
from student_list import StudentList
from file import FileManager


def test_add_sorted():
    sl = StudentList()
    sl.addNewStudent(Student("Bob", "1", "a", "1"))
    sl.addNewStudent(Student("Zak", "2", "b", "2"))
    sl.addNewStudent(Student("Emma", "3", "c", "3"))

    assert sl.students[0].name == "Bob"
    assert sl.students[1].name == "Emma"
    assert sl.students[2].name == "Zak"


def test_delete():
    sl = StudentList()
    sl.addNewStudent(Student("Bob", "1", "a", "1"))

    assert sl.deleteStudent("Bob") is True
    assert len(sl.students) == 0


def test_update():
    sl = StudentList()
    sl.addNewStudent(Student("Bob", "1", "a", "1"))

    updated = Student("Emma", "2", "b", "2")
    sl.updateStudent("Bob", updated)

    assert sl.students[0].name == "Emma"


def test_save_and_load():
    sl = StudentList()
    sl.addNewStudent(Student("Bob", "1", "a", "1"))

    fm = FileManager("test_out.csv")
    fm.save(sl.getAll())

    sl2 = StudentList()
    fm2 = FileManager("test_out.csv")
    fm2.load(sl2)

    assert len(sl2.students) == 1
    assert sl2.students[0].name == "Bob"
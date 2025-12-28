import csv
from student import Student

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self, student_list):
        try:
            with open(self.file_name, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.addNewStudent(
                        Student(row["name"], row["phone"], row["address"], row["date"])
                    )
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Using empty list.")

    def save(self, students):
        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "address", "date"])
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
        print("CSV saved.")
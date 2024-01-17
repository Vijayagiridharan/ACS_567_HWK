import csv
import statistics

from student_data import StudentData

class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def read_data(self):
        try:
            with open("students.csv", mode="r") as file:
                reader = csv.DictReader(file)
                self.students = [StudentData(row["Name"], int(row["Age"]), int(row["Grade"]), float(row["Attendance"])) for row in reader]
            print("Data read successfully.")
            print("Number of students:", len(self.students))
            print("student data:", self.students[:50])  
        except FileNotFoundError:
            print("File 'students.csv' not found. Make sure the file is in the correct location.")
        except Exception as e:
            print(f"An error occurred while reading data: {str(e)}")

    def write_data(self):
        with open("students.csv", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Grade", "Attendance"])
            writer.writeheader()
            writer.writerows([{"Name": student.name, "Age": student.age, "Grade": student.grade, "Attendance": student.attendance} for student in self.students])

    def add_student(self, student):
        self.students.append(student)
        self.write_data()

    def edit_student(self, old_name, new_student):
        for i, student in enumerate(self.students):
            if student.name == old_name:
                self.students[i] = new_student
                self.write_data()
                return True
        return False

    def delete_student(self, name):
        self.students = [student for student in self.students if student.name != name]
        self.write_data()

    def analyze_data(self):
        if not self.students:
            print("No data available.")
            return

        ages = [student.age for student in self.students]
        grades = [student.grade for student in self.students]
        attendance = [student.attendance for student in self.students]

        mean_age = statistics.mean(ages)
        median_grade = statistics.median(grades)
        mean_attendance = statistics.mean(attendance)

        print(f"Mean Age: {mean_age}")
        print(f"Median Grade: {median_grade}")
        print(f"Mean Attendance: {mean_attendance}")

    def filter_data_by_grade(self, grade):
        filtered_data = [student for student in self.students if student.grade == grade]
        return filtered_data

    def filter_data_by_attendance(self, min_attendance):
        filtered_data = [student for student in self.students if student.attendance >= min_attendance]
        return filtered_data

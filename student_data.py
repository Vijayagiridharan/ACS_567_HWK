
class StudentData:
    def __init__(self, name, age, grade, attendance):
        self.name = name
        self.age = age
        self.grade = grade
        self.attendance = attendance

    def __repr__(self):
       
        return f"(Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Attendance: {self.attendance})"

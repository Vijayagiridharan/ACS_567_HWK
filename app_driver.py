
from data_manager import DataManager
from student_data import StudentData

class AppDriver:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def print_menu(self):
        print("---------------------")
        print("Select an option:")
        print("1. Read Data from File")
        print("2. Add Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Analyze Data")
        print("6. Filter Data by Grade")
        print("7. Filter Data by Attendance")
        print("---------------------")

    def run(self):
        while True:
            self.print_menu()
            option = input("Please make a choice >> ")

            if option == "1":
                self.data_manager.read_data()
            elif option == "2":
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                grade = int(input("Enter student grade: "))
                attendance = float(input("Enter student attendance: "))
                new_student = StudentData(name, age, grade, attendance)
                self.data_manager.add_student(new_student)
            elif option == "3":
                old_name = input("Enter the name of the student to edit: ")
                new_name = input("Enter the new name: ")
                age = int(input("Enter the new age: "))
                grade = int(input("Enter the new grade: "))
                attendance = float(input("Enter the new attendance: "))
                new_student = StudentData(new_name, age, grade, attendance)
                if not self.data_manager.edit_student(old_name, new_student):
                    print("Student not found.")
            elif option == "4":
                name = input("Enter the name of the student to delete: ")
                self.data_manager.delete_student(name)
            elif option == "5":
                self.data_manager.analyze_data()
            elif option == "6":
                grade = int(input("Enter the grade to filter: "))
                filtered_data = self.data_manager.filter_data_by_grade(grade)
                self.display_data(filtered_data)
            elif option == "7":
                min_attendance = float(input("Enter the minimum attendance to filter: "))
                filtered_data = self.data_manager.filter_data_by_attendance(min_attendance)
                self.display_data(filtered_data)
            else:
                print("Invalid Option. Please try again.")

            input("Press enter to continue......")

    def display_data(self, data):
        print("Student Data:")
        if not data:
            print("No data to display.")
        else:
            for student in data:
                print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}, Attendance: {student.attendance}")


if __name__ == "__main__":
    data_manager_instance = DataManager()
    app = AppDriver(data_manager_instance)
    app.run()


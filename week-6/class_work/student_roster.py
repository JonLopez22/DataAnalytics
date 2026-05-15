class Student:
    school = "YearUp Academy"

    def __init__(self, name, grade, track): # init/instance attributes
        self.name = name
        self.__grade = grade #PRIVATE
        self.track = track

    def get_grade(self):        # Getter Method
        return self.__grade

    def set_grade(self, new_grade):      # Setter
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade! Must be 0-100.")

    def display_info(self):        # Display method with f-string
        print(f"""
===== YearUp Academy - Student Report =====
School : {Student.school}
Name   : {self.name}
Grade  : {self.get_grade()}
Track  : {self.track}
""")
# Call the object and methods
student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")
# print it out
print(student1.get_grade())
student1.set_grade(98)
student1.set_grade(150)
student1.display_info()
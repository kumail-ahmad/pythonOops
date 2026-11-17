class Student:
    studentName = ""
    rollNo = 0

    def displayDetails(self):
        print("Student Name:", self.studentName)
        print("Roll Number:", self.rollNo)


s1 = Student()
s1.studentName = "Rahul Sharma"
s1.rollNo = 101
s1.displayDetails()

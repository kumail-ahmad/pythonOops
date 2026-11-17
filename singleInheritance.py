class Person:
    def __init__(self, personName, personAge):
        self.personName = personName
        self.personAge = personAge

    def showPerson(self):
        print("Name:", self.personName)
        print("Age:", self.personAge)


class Teacher(Person):
    def __init__(self, personName, personAge, subjectName):
        super().__init__(personName, personAge)
        self.subjectName = subjectName

    def showTeacher(self):
        self.showPerson()
        print("Subject:", self.subjectName)


t1 = Teacher("Dr. Neha Gupta", 38, "Computer Networks")
t1.showTeacher()

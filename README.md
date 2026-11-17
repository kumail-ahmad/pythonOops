# Python Object-Oriented Programming (OOP) Assignment

---

### Program 1: Basic Class and Object Creation (`classAndObject.py`)

**Problem Statement:**  
Write a Python program to create a `Student` class with attributes `studentName` and `rollNo`. Create an instance of the class, assign values to its attributes, and display the details using an instance method.

```python
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
```

---

### Program 2: Constructors and Instance Methods (`constructorAndMethods.py`)

**Problem Statement:**  
Write a Python program to define a `BankAccount` class using a constructor (`__init__`) to initialize `accountHolder` and `accountBalance`. Include methods to deposit money and display the updated balance.

```python
class BankAccount:
    def __init__(self, accountHolder, accountBalance):
        self.accountHolder = accountHolder
        self.accountBalance = accountBalance

    def depositAmount(self, amount):
        self.accountBalance += amount
        print("Deposited:", amount)

    def displayBalance(self):
        print("Account Holder:", self.accountHolder)
        print("Current Balance:", self.accountBalance)


myAccount = BankAccount("Aman Verma", 5000)
myAccount.displayBalance()
myAccount.depositAmount(1500)
myAccount.displayBalance()
```

---

### Program 3: Single Inheritance (`singleInheritance.py`)

**Problem Statement:**  
Write a Python program to demonstrate single inheritance. Create a base class `Person` with attributes `personName` and `personAge`, and derive a subclass `Teacher` that adds `subjectName` and displays the complete information.

```python
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
```

---

### Program 4: Method Overriding and Polymorphism (`methodOverridingPolymorphism.py`)

**Problem Statement:**  
Write a Python program to demonstrate polymorphism via method overriding. Create a base class `Shape` with a method `calcArea()`, and override it in derived classes `Circle` and `Rectangle`. Iterate through a list of shape objects to call the overridden method dynamically.

```python
class Shape:
    def calcArea(self):
        print("Area calculation not defined for general shape.")


class Circle(Shape):
    def __init__(self, radiusValue):
        self.radiusValue = radiusValue

    def calcArea(self):
        area = 3.14 * self.radiusValue * self.radiusValue
        print("Area of Circle:", area)


class Rectangle(Shape):
    def __init__(self, rectLength, rectBreadth):
        self.rectLength = rectLength
        self.rectBreadth = rectBreadth

    def calcArea(self):
        area = self.rectLength * self.rectBreadth
        print("Area of Rectangle:", area)


shapesList = [Circle(5), Rectangle(4, 6)]

for item in shapesList:
    item.calcArea()
```

---

### Program 5: Code Reusability through Multilevel Inheritance (`multilevelInheritance.py`)

**Problem Statement:**  
Write a Python program to demonstrate code reusability using multilevel inheritance. Create a base class `Vehicle`, a child class `Car`, and a further derived class `ElectricCar`, reusing methods across the hierarchy.

```python
class Vehicle:
    def __init__(self, vehicleBrand):
        self.vehicleBrand = vehicleBrand

    def showBrand(self):
        print("Brand:", self.vehicleBrand)


class Car(Vehicle):
    def __init__(self, vehicleBrand, carModel):
        super().__init__(vehicleBrand)
        self.carModel = carModel

    def showModel(self):
        self.showBrand()
        print("Model:", self.carModel)


class ElectricCar(Car):
    def __init__(self, vehicleBrand, carModel, batteryCapacity):
        super().__init__(vehicleBrand, carModel)
        self.batteryCapacity = batteryCapacity

    def showCarDetails(self):
        self.showModel()
        print("Battery Capacity:", self.batteryCapacity, "kWh")


myCar = ElectricCar("Tata", "Nexon EV", 40.5)
myCar.showCarDetails()
```

---

### Program 6: File Handling with OOP (`fileHandlingReadWrite.py`)

**Problem Statement:**  
Write a Python program to create a `FileManager` class that manages file operations using OOP. Implement methods to write text data to a file and read data back from the file to print it on the console.

```python
class FileManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def writeData(self, textContent):
        fileObj = open(self.fileName, "w")
        fileObj.write(textContent)
        fileObj.close()
        print("Data written successfully.")

    def readData(self):
        fileObj = open(self.fileName, "r")
        fileContent = fileObj.read()
        fileObj.close()
        print("File Content:")
        print(fileContent)


fileHandler = FileManager("records.txt")
fileHandler.writeData("Roll No: 101\nName: Ankit Sharma\nBranch: CSE")
fileHandler.readData()
```

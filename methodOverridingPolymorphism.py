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

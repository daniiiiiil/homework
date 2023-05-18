class Figure:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print(self.width * self.height)

    def get_perimeter(self):
        print(2 * (self.width + self.height))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        per = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        print(per)

    def get_perimeter(self):
        print(self.side1 + self.side2 + self.side3)


triangle = Triangle(3, 4, 5)
triangle.get_area()
triangle.get_perimeter()

pramoykub = Rectangle(6, 8)
pramoykub.get_perimeter()
pramoykub.get_area()

square = Square(5)
square.get_area()
square.get_perimeter()

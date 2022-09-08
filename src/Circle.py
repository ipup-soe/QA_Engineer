import math
from src.Figure import Figure

class Circle(Figure):
    def __init__(self, r):
        super().__init__("Circle")
        self.r = r

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def area(self):
        return math.pi * self.r ** 2

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            raise ValueError
        return self.area() + obj.area()
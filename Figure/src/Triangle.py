import math
from src.Figure import Figure

class Triangle(Figure):
    #NAME = "Ttiangle"
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semiper = self.perimeter() / 2
        return math.sqrt(semiper * (semiper - self.a) * (semiper - self.b) * (semiper - self.c))

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            raise ValueError
        return self.area() + obj.area()

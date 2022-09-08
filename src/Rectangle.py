from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def area(self):
        return self.a * self.b

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            raise ValueError
        return self.area() + obj.area()
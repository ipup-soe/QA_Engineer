from src.Figure import Figure

class Square(Figure):
    def __init__(self, a):
        super().__init__("Square")
        self.a = a

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            raise ValueError
        return self.area() + obj.area()

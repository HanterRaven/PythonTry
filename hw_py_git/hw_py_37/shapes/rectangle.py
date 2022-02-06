class Rectangle:

    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        res = self.l * 2 + self.h * 2
        print(f"Периметр: {res}")
        return res

    def get_rect_aria(self):
        res = self.l * self.h
        print(f"Площадь: {res}")
        return res

    def print_rect(self):
        print(f"Стороны: {self.l},{self.h}")


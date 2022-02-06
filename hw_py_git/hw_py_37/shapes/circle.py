from math import pi


class Circle:

    def __init__(self, r):
        self.r = r

    def get_circle_square(self):
        res = pi * self.r ** 2
        print(f"Площадь круга: {round(res, 2)}")
        return res

    def get_circle_circumference(self):
        res = 2 * pi * self.r
        print(f"Длинна окружности: {round(res, 2)}")
        return res

    def print_circle(self):
        print(f"Радиус: {self.r}")

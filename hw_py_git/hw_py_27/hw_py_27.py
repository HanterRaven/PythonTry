import math


class Sphere:

    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_volume(self):
        return 4 / 3 * (math.pi * (self.radius ** 3))

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_center(self):
        return self.x, self.y, self.z

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        r1 = (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2
        if (self.radius ** 2) > r1:
            return True
        return False


sphere_1 = Sphere(0.6, 0, 0, 0)
print(f"get_radius : {sphere_1.get_radius()}")
print(f"get_volume : {sphere_1.get_volume()}")
print(f"get_square : {sphere_1.get_square()}")
print(f"get_center : {sphere_1.get_center()}")
print(f"get_square : {sphere_1.get_square()}")
print(f"is_point_inside(0, -1.5, 0) : {sphere_1.is_point_inside(0, -1.5, 0)}")
sphere_1.set_radius(1.6)
print(f"set_radius(1.6) : {sphere_1.get_radius()}")
print(sphere_1.is_point_inside(0, -1.5, 0))
print(f"is_point_inside(0, -1.5, 0) : {sphere_1.is_point_inside(0, -1.5, 0)}")

class ValidPoint:
    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Введено не целлочисленное значение")
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point3d:
    _x = ValidPoint()
    _y = ValidPoint()
    _z = ValidPoint()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def print_info(self):
        print(f"x = {self._x}, y = {self._y}, z = {self._z}")


p1 = Point3d(1, 2, 3)
p1.print_info()
p2 = Point3d(1.2, 2, 3)
p2.print_info()

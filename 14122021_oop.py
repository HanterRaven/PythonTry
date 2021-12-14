# __магический метод__
# специальные методоты
# конструктор __new__
# инициализатор  __init__
# деструктор  __del__
#

# class Point:
#     count = 0
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("Konstruktor")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Inicializator")
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     # def __del__(self):
#     #     print("Ydanenie " + self.__class__.__name__)
#
#
# p1 = Point(5, 7)
#
# print(p1.__dict__)
# Point.__init__(p1, 20)
# print(p1.x, p1.y)
# # p1 = 0
# # del p1
# print(p1.x)
# p2 = Point()
# print(p2.__dict__)
# # p3 = Point(22)
# # print(p3.__dict__)
# print(Point.count)
# print(p2.count)

#
#
# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.count += 1
#
#     def __del__(self):
#         Robot.count -= 1
#         if Robot.count == 0:
#             print(f"{self.name} выключается!")
#             print(f"{self.name} был последним")
#         else:
#             print(f"{self.name} выключается!")
#             print("Работающих роботов осталось", Robot.count)
#
#     def sey_hi(self):
#         print(f"Приветствую! меня зовут: {self.name}")
#         print("Численность роботов", Robot.count)
#
#
# droid1 = Robot("R2-d2")
# droid1.sey_hi()
# droid12 = Robot("C-3PO")
# droid12.sey_hi()
# print("Туту роботы чето делают")
# print("Нужно выключить роботов")
# del droid12
#
# del droid1
#
#
# class Point:
#
#     def __init__(self, x, y):
#         print("Inicializator")
#         self.__x = x
#         self.__y = y
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_coords(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def set_coord_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("VVedeno figna")
#
#     def set_coord_x(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("VVedeno figna")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
# p1 = Point(5, 10)
# # # print(p1._x, p1.__y)
# # # p1._x = 100
# # # p1.__y = "abc"
# # # print(p1._x, p1._y)
# # # x -public
# # # _x - protected
# # # __x - privat
# # p1.set_coords(13,17)
# # print(p1.get_coords())
# print(p1.__dict__)
# p1._Point__x=111
# print(p1._Point__x)


# class Rectangle:
#
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__width * self.__length
#
#     def perimetr(self):
#         return 2 * (self.__length * self.__width)
#
#     def hype(self):
#         return (self.__width ** 2 + self.__length ** 2) ** 0.5
#
#     def print_priam(self):
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle(3, 9)
# print(f"Visota -  {rec1.get_length()}")
# print(rec1.get_width())
# print(f"Square - {rec1.square()}")
# print(f"Perimetr {rec1.perimetr()}")
# print(f"Gipotynuza {round(rec1.hype(), 2)}")
# rec1.print_priam()


class Point:
    WIDTH = 5
    z = 100

    def __init__(self, x, y):
        print("Inicializator")
        self.__x = x
        self.__y = y

    # def __getattr__(self, item):
    #     return f" V classe {__class__.__name__} net atribut {item}"

    # def __getattribute__(self, item):
    #     if item == "_Point__x":
    #         return "Peremennaya zakrita"
    #     else:
    #         return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError
        else:
            self.__dict__[key] = value

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def set_coord_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("VVedeno figna")

    def set_coord_x(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("VVedeno figna")

    def get_coords_x(self):
        return self.__x

    def get_coords_y(self):
        return self.__y

    def area(self):
        return (self.__x + Point.WIDTH)+self.z


p1 = Point(5, 10)
# print(p1.zzz)
# print(p1.__dict__)
# p1._Point__x = 111
# print(p1._Point__x)
# print(p1.get_coords())
p1.z = 100
Point.WIDTH = 10
print(p1.area())

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         print("Inicializator")
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)
#

# class Point:
#
#     def __init__(self, x, y):
#         print("Inicializator")
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property
#     def coords_x(self):
#         print("get")
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             print("set")
#             self.__x = x
#         else:
#             print("neverniy format dannix")
#
#     @coords_x.deleter
#     def coord_x(self):
#         print("udalenie svoistva")
#         del self.__x
#
#     # coord_x = property(__get_coords_x, __set_coords_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 101
# print(p1.coord_x)

#
# class Convert_to_pounds:
#
#     def __init__(self, kg):
#         self.kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Vveli ne to")
#
#     def convert_pounds(self):
#         return f"{self.__kg} кг = > {self.__kg * 2.205}"
#
#
# kilo = Convert_to_pounds(12)
# print(kilo.convert_pounds())
# kilo.kg = 41
# print(kilo.convert_pounds())

#
# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         print("Inicializator")
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))
#
#
# class Math_metod:
#
#     @staticmethod
#     def minimum(x, y, z, n):
#         if x < y and x < z and x < n:
#             return f"Minimum : {x}"
#         if y < x and y < z and y < n:
#             return f"Minimum : {y}"
#         if z < y and z < x and z < n:
#             return f"Minimum : {z}"
#         if n < y and n < z and n < x:
#             return f"Minimum : {n}"
#
#     @staticmethod
#     def maximum(x, y, z, n):
#         if x > y and x > z and x > n:
#             return f"Maximun : {x}"
#         if y > x and y > z and y > n:
#             return f"Maximun : {y}"
#         if z > y and z > x and z > n:
#             return f"Maximun : {z}"
#         if n > y and n > z and n > x:
#             return f"Maximun : {n}"
#
#     @staticmethod
#     def srednee(x, y, z, n):
#         return f"Srednee : {(x + y + z + n) / 4}"
#
#     @staticmethod
#     def faktorial(x):
#         fac = 1
#         for i in range(1, x + 1):
#             fac *= i
#         return f"Factorial {fac}"
#
#
# print(Math_metod.minimum(2, 3, 4, 5))
# print(Math_metod.maximum(2, 3, 4, 5))
# print(Math_metod.srednee(2, 3, 4, 5))
# print(Math_metod.faktorial(5))

#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         print(date1)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string1):
#         if date_as_string1.count(".") == 2:
#             day, month, year = map(int, date_as_string1.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # d = "16.12.2021"
# # # day, month, year = map(int, d.split("."))
# # # date = Date(day, month, year)
# # # print(date.string_to_db())
# # d = Date()
# # date = d.from_string("16.14.2021")
# # print(date.string_to_db())
# dates = ["30.12.2021", "30-12-2021", "01.01.2021", "12.31.2020"]
# for j in dates:
#     if Date.is_date_valid(j):
#         date = Date.from_string(j)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print("Ne pravolnaya data ili format stroki")
#
#
#
#
# class Ploshad:
#     count = 0
#
#     @staticmethod
#     def rectangle_Geron(a, b, c):
#         Ploshad.count += 1
#         perimetr = (a + b + c) / 2
#         return (perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)) ** 0.5
#
#     @staticmethod
#     def osnovanie_visota(a, h):
#         Ploshad.count += 1
#         return 0.5 * h * a
#
#     @staticmethod
#     def ploshad_sq(a):
#         Ploshad.count += 1
#         return a ** 2
#
#     @staticmethod
#     def ploshad_pryam(a, b):
#         Ploshad.count += 1
#         return a * b
#
#
# print(Ploshad.rectangle_Geron(3, 4, 5))
# print(Ploshad.osnovanie_visota(6, 7))
# print(Ploshad.ploshad_sq(7))
# print(Ploshad.ploshad_pryam(2, 6))
# try_t = Ploshad()
# print(try_t.rectangle_Geron(1, 2, 3))
# print(Ploshad.count)

# class Point:
#     """Класс для представления точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# #
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
# #
#
# p1 = Point()
# p2 = Point()
# p1.x = 5
# p1.y = 7
#
# # # Point.x = 100
# #
# # print(p1.x)
# # p1.x = 5
# # p1.y = 10
# # # p1.z = 20
# # print(p1.x, Point.x)
# # # print(p1.__dict__)
# # # print(Point.__dict__)
# # print(getattr(p1, "z", "False"))
# # print(getattr(p1, "x"))
# # setattr(p1, "z", 7)
# # print(hasattr(p1, "x"))
# # print(hasattr(p1, "z"))
# # p2 = Point()
# # delattr(p1, "z")
# # print(p2.__dict__)
# # print(p1.__dict__)
# # print(type(p1) == Point)
# # print(isinstance(p1, Point))
# p1.set_coords(3, 8)
# p2.set_coords(10, 20)
# Point.set_coords(p1, 4, 9)
# print(p1.__dict__)
#
# class Human:
#     name = "Try name"
#     date = "01.01.1970"
#     phone_number = "80 - 800 - 200"
#     country = "Arctic"
#     town = "City"
#     home_address = "Ziro streen 00 "
#
#     def get_allatr(self, name, date, phone_number, country, town, home_adress):
#         self.name = name
#         self.date = date
#         self.phone_number = phone_number
#         self.country = country
#         self.town = town
#         self.home_address = home_adress
#
#     def print_info(self):
#         print(" Персоональные данные".center(40, "*"))
#         print(
#             f"Имя: {self.name}\nдата рождения: {self.date}\nНомер телефона: {self.phone_number}\nСтрана: {self.country}\n"
#             f"Город: {self.town}\nДомашний адрес: {self.home_address}")
#         print("=" * 40)
#
#     def get_name(self, name):
#         self.name = name
#
#     def get_date(self, date):
#         self.date = date
#
#     def get_phone(self, phone_number):
#         self.phone_number = phone_number
#
#     def get_country(self, country):
#         self.country = country
#
#     def get_town(self, town):
#         self.town = town
#
#     def get_address(self, home_address):
#         self.home_address = home_address
#
#     def set_name(self):
#         return self.name
#
#     def set_date(self):
#         return self.date
#
#     def set_phone(self):
#         return self.phone_number
#
#     def set_country(self):
#         return self.country
#
#     def set_town(self):
#         return self.town
#
#     def set_address(self):
#         return self.home_address
#
#
# hum = Human()
# hum.print_info()

#
# class Auto:
#     model = "xx m00i"
#     date = 1970
#     creator = "XXX"
#     power = "000 ls"
#     color = "White"
#     price = "000000000"
#
#     def set_all(self, model, date, creator, power, color, price):
#         self.model = model
#         self.date = date
#         self.creator = creator
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def auto_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\n"
#               f"Год выпуска: {self.model}\n"
#               f"Производитель: {self.model}\n"
#               f"Мощность двигателя: {self.model}\n"
#               f"Цвет машины: {self.model}\n"
#               f"Цена: {self.model}"
#               )
#         print("*" * 40)
#
#     def set_model(self, model):
#         self.model = model
#
#     def set_date(self, date):
#         self.date = date
#
#     def set_creator(self, creator):
#         self.creator = creator
#
#     def set_power(self, power):
#         self.power = power
#
#     def set_color(self, color):
#         self.color = color
#
#     def set_price(self, price):
#         self.price = price
#
#     def det_model(self):
#         return self.model
#
#     def get_date(self):
#         return self.date
#
#     def get_creator(self):
#         return self.creator
#
#     def get_power(self):
#         return self.power
#
#     def get_color(self):
#         return self.color
#
#     def get_price(self):
#         return self.price
#
#
# ta4ka = Auto()
# ta4ka.auto_info()
# ta4ka.set_color("red")
# print(ta4ka.get_color())
# ta4ka.set_all("X7 M50i", 2021, "BMW", "520 ls", "White", "10790000")
# ta4ka.auto_info()

class Person:
    grade = 1

    def write_all(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Данные Сотрудника {self.name} {self.surname}")

    def set_grade(self, grade):
        self.grade = self.grade + grade
        print(f"Квалификация сотрудника {self.grade}")


p1 = Person()
p1.write_all("Kata", "Reznik")
p1.set_grade(12)
p2 = Person()
p2.write_all("Anna", "Dolgih")
p2.set_grade(10)
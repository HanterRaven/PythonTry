class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def summ_a_b(self):
        return self.a + self.b

    def multi_a_b(self):
        return self.a * self.b


class Right_Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def gipotenusa(self):
        return round(((self.a ** 2 + self.b ** 2) ** 0.5), 2)

    def print_info(self):
        print(f"Прямоугольный треугольник ABC ({self.a}, {self.b}, {self.gipotenusa()})")

    def square(self):
        return round(1 / 2 * self.a * self.b, 2)


triangl1 = Right_Triangle(5, 8)
print(f"Гипотенуза ABC : {triangl1.gipotenusa()}")
triangl1.print_info()
print(f"Площадь треугольника ABC : {triangl1.square()}")
print()
print(f"Сумма : {triangl1.summ_a_b()}")
print(f"Произведение : {triangl1.multi_a_b()}")
triangl1.a = 10
print()
print(f"Гипотенуза ABC : {triangl1.gipotenusa()}")
triangl1.b = 20
print(f"Гипотенуза ABC : {triangl1.gipotenusa()}")
print(f"Сумма : {triangl1.summ_a_b()}")
print(f"Произведение : {triangl1.multi_a_b()}")
print(f"Площадь треугольника ABC : {triangl1.square()}")

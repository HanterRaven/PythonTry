# если шаблон ввода линейного уравнения ax знак b = c
# и шаблон квадратного ax^2 знак bx знак c = 0

from abc import ABC, abstractmethod


class Root(ABC):
    def __init__(self, get_string):
        self.get_string = get_string
        self.result = 0

    @abstractmethod
    def print_rezult(self):
        print(f"'{self.get_string}' is {self.result}")

    @abstractmethod
    def description(self):
        pass


class SingleRoot(Root):
    def __init__(self, get_string):
        super().__init__(get_string)

    def description(self):
        perem = []
        temp = ""
        znak = []
        for i in self.get_string:
            if i != "+" and i != "-" and i != "=":
                temp += i
            else:
                znak.append(i)
                perem.append(temp)
                temp = ""
        else:
            perem.append(temp)
        for i in range(len(perem)):
            if perem[i].find("x") != -1:
                if perem[i].index("x") == 0:
                    perem[i] = "1"
                else:
                    perem[i] = perem[i][0:perem[i].index("x")]
        for i in znak:
            if i == "+":
                self.result = round(((int(perem[2]) - int(perem[1])) / int(perem[0])), 2)
            elif i == "/":
                self.result = (int(perem[2]) * int(perem[1])) / int(perem[0])
            elif i == "-":
                self.result = (int(perem[2]) + int(perem[1])) / int(perem[0])
            elif i == "*":
                self.result = int(perem[2]) / (int(perem[0]) * int(perem[1]))

    def print_rezult(self):
        print(f"The root of ", end="")
        super().print_rezult()


class SquareRoot(Root):
    def __init__(self, get_string):
        super().__init__(get_string)

    def description(self):
        perem = []
        temp = ""
        znak = []
        x1, x2 = 0, 0
        for i in self.get_string:
            if i != "+" and i != "-" and i != "=":
                temp += i
                x1 = 1
            else:
                if x1 == 0:
                    temp += i
                    x1 = 1
                else:
                    znak.append(i)
                    perem.append(temp)
                    temp = ""
        else:
            perem.append(temp)
        for i in range(len(perem)):
            if perem[i].find("x") != -1:
                if perem[i].index("x") == 0:
                    perem[i] = "1"
                elif perem[i].index("x") == 1 and perem[i] == "-x":
                    perem[i] = "-1"
                else:
                    perem[i] = perem[i][0:perem[i].index("x")]
        if znak[0] == "-":
            perem[1] = int(perem[1]) * (-1)
        if znak[1] == "-":
            perem[2] = int(perem[2]) * (-1)
        deskr = (int(perem[1]) ** 2) - (4 * int(perem[0]) * int(perem[2]))
        if deskr < 0:
            self.result = "Корней нет"
        elif deskr == 1:
            self.result = round((-1 * perem[1]) / (2 * perem[0]), 2)
        elif deskr > 1:
            x1 = (-1 * int(perem[1]) + (deskr ** 0.5)) / (2 * int(perem[0]))
            x2 = (-1 * int(perem[1]) - (deskr ** 0.5)) / (2 * int(perem[0]))
        self.result = str(x1) + "  " + str(x2)

    def print_rezult(self):
        print(f"The roots of ", end="")
        super().print_rezult()


test = SingleRoot("3x+7=0")
test_1 = SquareRoot("1x^2-2x-3=0")
test.description()
test.print_rezult()
print()
test_1.description()
test_1.print_rezult()

# или
# from abc import ABC, abstractmethod
#
#
# class Root(ABC):
#     def __init__(self, get_string):
#         self.get_string = get_string
#         self.result = 0
#
#     @abstractmethod
#     def print_rezult(self):
#         pass
#
#     @abstractmethod
#     def description(self):
#         pass
#
#
# class SingleRoot(Root):
#     def __init__(self, get_string):
#         super().__init__(get_string)
#
#     def description(self):
#         perem = []
#         temp = ""
#         znak = []
#         for i in self.get_string:
#             if i != "+" and i != "-" and i != "=":
#                 temp += i
#             else:
#                 znak.append(i)
#                 perem.append(temp)
#                 temp = ""
#         else:
#             perem.append(temp)
#         for i in range(len(perem)):
#             if perem[i].find("x") != -1:
#                 if perem[i].index("x") == 0:
#                     perem[i] = "1"
#                 else:
#                     perem[i] = perem[i][0:perem[i].index("x")]
#         for i in znak:
#             if i == "+":
#                 self.result = round(((int(perem[2]) - int(perem[1])) / int(perem[0])), 2)
#             elif i == "/":
#                 self.result = (int(perem[2]) * int(perem[1])) / int(perem[0])
#             elif i == "-":
#                 self.result = (int(perem[2]) + int(perem[1])) / int(perem[0])
#             elif i == "*":
#                 self.result = int(perem[2]) / (int(perem[0]) * int(perem[1]))
#
#     def print_rezult(self):
#         print(f"The root of '{self.get_string}' is {self.result}")
#
#
# class SquareRoot(Root):
#     def __init__(self, get_string):
#         super().__init__(get_string)
#
#     def description(self):
#         perem = []
#         temp = ""
#         znak = []
#         x1, x2 = 0, 0
#         for i in self.get_string:
#             if i != "+" and i != "-" and i != "=":
#                 temp += i
#                 x1=1
#             else:
#                 if x1 == 0:
#                     temp += i
#                     x1 = 1
#                 else:
#                     znak.append(i)
#                     perem.append(temp)
#                     temp = ""
#         else:
#             perem.append(temp)
#         for i in range(len(perem)):
#             if perem[i].find("x") != -1:
#                 if perem[i].index("x") == 0:
#                     perem[i] = "1"
#                 elif perem[i].index("x") == 1 and perem[i] == "-x":
#                     perem[i] = "-1"
#                 else:
#                     perem[i] = perem[i][0:perem[i].index("x")]
#         if znak[0] == "-":
#             perem[1] = int(perem[1]) * (-1)
#         if znak[1] == "-":
#             perem[2] = int(perem[2]) * (-1)
#         deskr = (int(perem[1]) ** 2) - (4 * int(perem[0]) * int(perem[2]))
#         if deskr < 0:
#             self.result = "Корней нет"
#         elif deskr == 1:
#             self.result = round((-1 * perem[1]) / (2 * perem[0]), 2)
#         elif deskr > 1:
#             x1 = (-1 * int(perem[1]) + (deskr ** 0.5)) / (2 * int(perem[0]))
#             x2 = (-1 * int(perem[1]) - (deskr ** 0.5)) / (2 * int(perem[0]))
#         self.result = str(x1) + "  " + str(x2)
#
#     def print_rezult(self):
#         print(f"The roots of '{self.get_string}' is {self.result}")
#
#
# test = SingleRoot("3x+7=0")
# test_1 = SquareRoot("1x^2-2x-3=0")
# test.description()
# test.print_rezult()
# print()
# test_1.description()
# test_1.print_rezult()

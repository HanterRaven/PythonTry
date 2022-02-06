class Person:
    def __init__(self, surname: str, name: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"({self.surname},{self.name},{self.age})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Введено не строковое значение")
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise ValueError("Введено не строковое значение")
        self.__surname = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Введено не целочисленное значение")
        self.__age = value

    def __lt__(self, other):
        if (self.surname < other.surname) or (self.name < other.name):
            return True
        return False

    def __gt__(self, other):
        if (self.surname > other.surname) or (self.name > other.name):
            return True
        return False

    def __eq__(self, other):
        if (self.surname == other.surname) or (self.name == other.name):
            return True
        return False

    def __len__(self):
        return len(self.name)


class SortKey:
    def __init__(self, first, second=None):
        self.first = first
        self.second = second

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        self.__second = value

    def __call__(self, *args, **kwargs):
        if self.first == "surname" and self.second == "forename":
            for j in range(len(args[0])):
                for i in range(1, len(args[0])):
                    if (args[0][i - 1].surname > args[0][i].surname) or (
                            args[0][i - 1].surname == args[0][i].surname and
                            args[0][i - 1].name > args[0][i].name):
                        args[0][i - 1], args[0][i] = args[0][i], args[0][i - 1]
        if self.first == "surname" and self.second is None:
            for j in range(len(args[0])):
                for i in range(1, len(args[0])):
                    if args[0][i - 1].surname > args[0][i].surname:
                        args[0][i - 1], args[0][i] = args[0][i], args[0][i - 1]
        for i in args[0]:
            print(i)


p = [Person("Иванов", "Игорь", 28),
     Person("Петров", "Степан", 21),
     Person("Сидоров", "Антон", 25),
     Person("Петров", "Анатолий", 11),
     Person("Иванов", "Иван", 28)
     ]

t = SortKey("surname")
t(p)
print()
t1 = SortKey("surname", "forename")
t1(p)

# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#     @property
#     def data(self):
#         return self.surname, self.name, self.age
#
#     def __str__(self):
#         return f"{self.surname}, {self.name}, {self.age}"
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#     def __call__(self, lst):
#         lst.sort(key=lambda j: [j.__dict__[key] for key in self.__method])
#
#
# p = [Person("Иванов", "Игорь", 28), Person("Петров", "Степан", 21),
#      Person("Сидоров", "Антон", 25), Person("Петров", "Анатолий", 11), Person("Иванов", "Иван", 28)]
#
# for i in p:
#     print(i.data)
# print()
#
# s1 = SortKey('surname')
# s1(p)
# for i in p:
#     print(i.data)
# print()
#
# s2 = SortKey('surname', 'name')
# s2(p)
# for i in p:
#     print(i.data)
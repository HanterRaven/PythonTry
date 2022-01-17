class Student:
    def __init__(self, name):
        self._name = name
        self.noutbook = self.Noutbook()

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     self._name = name

    def print_info(self):
        print(f"{self._name} => {self.noutbook.model()}, {self.noutbook.cpu()}, {self.noutbook.memory()} ")

    class Noutbook:

        def model(self):
            return "HP"

        def cpu(self):
            return "Core-i7"

        def memory(self):
            return "16"


s1 = Student("Roman")
s1.print_info()
# s1.name = "Vladimir"
# s1.print_info()
s2 = Student("Vladimir")
s2.print_info()

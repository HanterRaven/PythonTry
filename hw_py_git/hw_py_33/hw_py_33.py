class Clock:
    __Day = 86400  # число секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Cекунды должны быть целым числом")

        self.__secs = secs % self.__Day

    def get_format_time(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __gt__(self, other):
        if self.__secs > other.__secs:
            return True
        return False

    def __ge__(self, other):
        if self.__secs >= other.__secs:
            return True
        return False

    def __lt__(self, other):
        if self.__secs < other.__secs:
            return True
        return False

    def __le__(self, other):
        if self.__secs <= other.__secs:
            return True
        return False


c1 = Clock(100)
print(c1.get_format_time())
c2 = Clock(100)
print(c2.get_format_time())
c3 = Clock(300)
print(c3.get_format_time())

print(f"c3 > c1 {c3 > c1}")
print(f"c3 >= c1 {c3 >= c1}")
print(f"c3 < c1 {c3 < c1}")
print(f"c3 <= c1 {c3 <= c1}")

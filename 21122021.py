class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix_ry = "RUB"
    suffix_usd = "USD"
    suffix_eu = "EUR"

    def __init__(self, name, schet, pesent, summ_py=0):
        self.name = name
        self.schet = schet
        self.pesent = pesent
        self.summ_py = summ_py
        print(f"Счет {self.schet} принадлежащий {self.name}  был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет {self.schet} принадлежащий {self.name}  был закрыт.")
        print("ваш счет закрыт!!!")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_euro = rate

    def convert_usd(self):
        usd_val = Account.convert(self.summ_py, Account.rate_usd)
        print(f"Состояние счета {usd_val} {Account.suffix_usd}")

    def convert_eur(self):
        usd_val = Account.convert(self.summ_py, Account.rate_euro)
        print(f"Состояние счета {usd_val} {Account.suffix_eu}")

    def print_balance(self):
        print(f"Текущий баланс {self.summ_py} {Account.suffix_ry}")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"№ счета - {self.schet}\nВладелец - {self.name}")
        self.print_balance()
        print(f"Процент - {self.pesent:.0%}")
        print("-" * 20)

    def change_name(self, new_name):
        self.name = new_name

    def get_deposit(self, get_money):
        if get_money <= self.summ_py:
            self.summ_py -= get_money
            print(f"Вы сняли {get_money} {Account.suffix_ry}.На счету осталось {self.summ_py} {Account.suffix_ry}")
        else:
            print(f"ВЫ хотите снять {get_money} {Account.suffix_ry} а у вас всего {self.summ_py} {Account.suffix_ry}")

    def set_persent(self):
        self.summ_py += self.summ_py * self.pesent
        print("Процент начислен!!!")
        self.print_balance()

    def add_money(self, money):
        self.summ_py += money
        print(f"{money} было успешно добавлено")
        self.print_balance()


acc1 = Account("Ktoto", "12345", 0.03, 1000)
acc1.print_info()
acc1.convert_usd()
acc1.convert_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc1.convert_usd()
acc1.convert_eur()

acc1.change_name("Duma")
acc1.set_persent()
acc1.print_info()
acc1.get_deposit(1500)
print()
acc1.get_deposit(700)
print()
acc1.add_money(5000)
print()

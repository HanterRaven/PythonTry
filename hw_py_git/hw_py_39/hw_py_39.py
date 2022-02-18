import json


class Country:
    def __init__(self, file_name):
        self.file_name = file_name
        self.country_list = {}
        self.exit = True

    @staticmethod
    def print_command_list():
        print(f"Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
              f"4 - редактированние данных\n5 - сохранение данных\n6 - просмотр данных\n7 - Загрузка данных\n"
              f"для выхода введите любое отсутствующее значение")
        print()

    @staticmethod
    def get_command():
        return int(input("Ввод команды - "))

    def add_string(self):
        country_name = str(input("Введите название страны - "))
        country_capital = str(input("Введите столицу - "))
        if self.find_country(country_name):
            print("Введите другое значение")
        else:
            self.country_list[country_name] = country_capital
            print("Запись добавлена")

    def del_string(self, count_name):
        temp = self.country_list.pop(count_name, None)
        if temp is None:
            print("Нет такой страны")

    def change_string(self, count_name):
        if self.find_country(count_name):
            print(self.country_list[count_name])
            print("Введите новые значения:")
            self.del_string(count_name)
            self.add_string()
        else:
            print("Такой страны нет")

    def find_country(self, country_name):
        if self.country_list.get(country_name) is None:
            print("Такой страны нет")
            return False
        else:
            print("Страна присутствует в списке")
            return True

    def write_json(self, person_dict):
        try:
            data = json.load(open(self.file_name))
            data.update(person_dict)
            with open(self.file_name, "w") as fil:
                json.dump(person_dict, fil, indent=2)
        except FileNotFoundError:
            with open(self.file_name, "w") as fil:
                json.dump(person_dict, fil, indent=2)

    def load_json(self):
        try:
            data = json.load(open(self.file_name))
            self.country_list.update(data)
        except FileNotFoundError:
            print("Файл отсутствует")


    def print_country(self):
        print("*"*30)
        for i, j in self.country_list.items():
            print(f"{i} - {j}")
        print("*" * 30)

    def work_command(self, command):
        if command == 1:
            self.add_string()
        elif command == 2:
            self.del_string(str(input("Введита название удаляемой страны - ")))
        elif command == 3:
            self.find_country(str(input("Введита название искомой страны - ")))
        elif command == 4:
            self.change_string(str(input("Введита название изменяемой страны - ")))
        elif command == 5:
            self.write_json(self.country_list)
        elif command == 6:
            self.print_country()
        elif command == 7:
            self.load_json()
        else:
            print("Нет такой команды")
            self.exit = False


new_contry = Country("country.json")
while new_contry.exit:
    new_contry.print_command_list()
    new_contry.work_command(Country.get_command())

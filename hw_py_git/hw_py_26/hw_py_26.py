class Book:
    title = "No name"
    year = "1970"
    publisher = "Publisher"
    genre = "all"
    author = "Ivan Ivanich Ivanov"
    price = "999999.99"

    def set_all_atribut(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def print_all_info(self):
        print(" Информация о книге ".center(40, "*"))
        print(f"Название книги = {self.title}\nГод выпуска - {self.year}\nИздатель - {self.publisher}\n"
              f"Жанр книги - {self.genre}\nАвтор книги - {self.author}\nЦена книги - {self.price} руб")
        print("*" * 40)

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


book1 = Book()
book1.set_all_atribut("Гарри поттер", "1997", "HBO", "Фентези", "Джуан Роулинг", "999")
# print(book1.__dict__)
book1.print_all_info()
book1.set_title("Властелин колец")
book1.set_year("1954")
book1.set_publisher("George Allen & Unwin")
book1.set_genre("Фентези!!")
book1.set_author("Р.Р. Толкин")
book1.set_price("1000")
print(book1.get_title())
print(book1.get_year())
print(book1.get_publisher())
print(book1.get_genre())
print(book1.get_author())
print(book1.get_price(), "руб")

def add_title(title):
    def wrapper(funk):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = funk(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        print("Действия с фильмами:")

        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенноого фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма:")
    def add_user_articles(self):
        dict_films = {"название": None, "жанр": None, "режисер": None, "год выпуска": None,
                      "длительность": None, "студия": None, "актеры": None}
        for i in dict_films:
            dict_films[i] = input(f"Введите {i} фильма :")
        return dict_films

    @add_title("Список фильмов")
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_films = input("Введите название фильма: ")
        return user_films

    @add_title("Просмотр фильма: ")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма:")
    def remove_single_film(self, film):
        print(f"Фильм {film} -была удаленв")

    @add_title("Сообщение об ошибке")
    def show_correct_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

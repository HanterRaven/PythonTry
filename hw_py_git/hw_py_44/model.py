import pickle
import os


class Film:
    def __init__(self, title, genre, director, year, time, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre} , {self.year})"


class FilmModel:
    def __init__(self):
        self.db_name = "db_name.txt"
        self.films = self.load_data()

    def add_film(self, dict_films):
        film = Film(*dict_films.values())
        self.films[film.title] = film

    def get_all_articles(self):
        return self.films.values()

    def get_single_article(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режисер": film.director,
            "год выпуска": film.year,
            "длительность": film.time,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

from view import UserInterface
from model import FilmModel


class Controller:
    def __init__(self):
        self.article_model = FilmModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None

        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            article = self.user_interface.add_user_articles()
            self.article_model.add_film(article)
        elif answer == "2":
            articles = self.article_model.get_all_articles()
            self.user_interface.show_all_films(articles)
        elif answer == "3":
            article_title = self.user_interface.get_user_film()
            try:
                article = self.article_model.get_single_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.show_single_film(article)
        elif answer == "4":
            article_title = self.user_interface.get_user_film()
            try:
                title = self.article_model.remove_film(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.remove_single_film(title)
        elif answer == "q":
            self.article_model.save_data()
        else:
            self.user_interface.show_correct_answer_error(answer)



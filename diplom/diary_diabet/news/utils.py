from news.models import *
from diary_pages.models import *

from django.db.models import Count

menu = [
    {'title': 'Новости', 'url_name': 'index'},
    {'title': 'Добавить пост', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Дневник', 'url_name': 'diary_page'},
    {'title': 'Добавить запиcь', 'url_name': 'add_diary_page'},

]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):

        context = kwargs
        cats = Category.objects.annotate(Count('news'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)
            user_menu.pop(3)
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


class DiaDataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)
            user_menu.pop(3)
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cat_selected'] = 'dia'
        return context

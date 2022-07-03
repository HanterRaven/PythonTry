from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.models import User

from news.utils import *
from .models import *
from .forms import *


# Create your views here.


class DiaryPage(DataMixin, ListView):
    model = Diary
    template_name = 'diary/diary.html'
    context_object_name = 'diary_page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Дневник')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Diary.objects.all()


class AddDiaryPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDiaryForm
    template_name = 'diary/adddiarypage.html'
    success_url = reverse_lazy('diary_page')
    login_url = reverse_lazy('diary_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Добавление записи')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):

        if self.request.method == 'GET':

            return render(self.request, 'news/adddiarypage.html', {'form': AddDiaryForm()})
        else:
            try:

                form = AddDiaryForm(self.request.POST)

                new_todo = form.save(commit=False)
                new_todo.dia_user = self.request.user
                new_todo.save()
                return redirect('diary_page')
            except ValueError:
                return HttpResponse('Найден не корректный заголовок')


class ShowRecord(DataMixin, DetailView):
    model = Diary
    template_name = 'diary/show_record.html'
    context_object_name = 'show_record'
    # slug_url_kwarg = 'id_user'
    pk_url_kwarg = 'id_user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='show_record')

        return dict(list(context.items()) + list(c_def.items()))


class RecordEdit(DataMixin, UpdateView):
    model = Diary
    template_name = 'diary/edit_record.html'
    context_object_name = 'record_edit'
    pk_url_kwarg = 'id_user'
    fields = ['food_intake', 'glucoza', 'he', 'insulin', 'food', 'date_food', 'time_food']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Редактирование записи')

        return dict(list(context.items()) + list(c_def.items()))

    # def form_valid(self, form):
    #     print('12312312231')
    #     post = get_object_or_404(form)
    #     if self.request.method == "POST":
    #         form = AddDiaryForm(self.request.POST)
    #         if form.is_valid():
    #             post = form.save(commit=False)
    #             post.dia_user = self.request.user
    #             post.save()
    #             return redirect('diary_page')
    #     else:
    #         form = AddDiaryForm(instance=post)
    #     return render(self.request, 'diary/edit_form.html', {'form': form})

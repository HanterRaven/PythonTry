from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.models import User

import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np
import random

from news.utils import *
from .models import *
from .forms import *


# Create your views here.


class DiaryPage(DiaDataMixin, ListView):
    model = Diary
    template_name = 'diary/diary.html'
    context_object_name = 'diary_page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Дневник')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Diary.objects.all()


class AddDiaryPage(LoginRequiredMixin, DiaDataMixin, CreateView):
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


# class ShowRecord(DiaDataMixin, DetailView):
#     model = Diary
#     template_name = 'diary/show_record.html'
#     context_object_name = 'show_record'
#     pk_url_kwarg = 'id_user'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         c_def = self.get_user_context(title='Запись')
#
#         return dict(list(context.items()) + list(c_def.items()))


class RecordEdit(DiaDataMixin, UpdateView):
    model = Diary
    template_name = 'diary/edit_record.html'
    context_object_name = 'record_edit'
    pk_url_kwarg = 'id_user'
    fields = ['food_intake', 'glucoza', 'he', 'insulin', 'food', 'date_food', 'time_food']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Редактирование записи')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return redirect('diary_page')


class Diagram(DiaDataMixin, ListView):
    model = Diary
    template_name = 'diary/diagram.html'
    context_object_name = 'diagram'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Редактирование записи')

        # plt.plot(range(10))
        if self.request.method == "POST":
            test_m = self.request.POST.get('name')
            print(test_m)

        try_t = []
        try_dia = Diary.objects.all().filter(dia_user__exact=self.request.user)
        try_dia = try_dia.order_by('time_food')[::-1]
        print([p.he for p in try_dia])
        print([p.glucoza for p in try_dia])
        print([p.insulin for p in try_dia])
        print([str(p.date_food) + ' ' + str(p.time_food) for p in try_dia])

        t_time = [str(p.date_food) + ' ' + str(p.time_food) for p in try_dia]
        t_g = [p.glucoza for p in try_dia]
        t_ins = [p.insulin for p in try_dia]
        t_he = [p.he for p in try_dia]
        for i in range(100):
            try_t.append(random.randint(0, 20))

        t = np.arange(0.0, 10.0, 0.1)
        print(t[1])
        s = try_t

        fig, ax = plt.subplots()
        ax.plot(t_time, t_g, 'o-b', t_time, t_he, 'o-.m', t_time, t_ins, 'og')

        ax.grid()

        fig = plt.gcf()

        plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=5)
        plt.legend(['глюкоза', 'Хе', 'инсулин'])
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        m_def = self.get_user_context(data=uri)

        return dict(list(context.items()) + list(c_def.items()) + list(m_def.items()))


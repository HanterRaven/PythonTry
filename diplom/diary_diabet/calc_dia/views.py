from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.http import HttpResponse
from .forms import UserForm
from news.forms import *
from .models import *
from news.utils import *


# class CalcDia(DiaDataMixin, UserForm, FormView):
#     forms = UserForm
#     template_name = 'calc.html'
#     context_object_name = 'cal'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         c_def = self.get_user_context(title='Калькулятор')
#
#         return dict(list(context.items()) + list(c_def.items()))

def calc_dia(request):
    # def form_valid(self, form):
    list_f = BaseFood.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        list_f = list_f.filter(c_name=name)
        test_he1 = [p.c_he for p in list_f]
        test_he = test_he1[0]
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Продукт, {0}</h2>"
                            "<p> в 100 граммах {1} Хе</p>"
                            "<p><a href=''>Назад</a</p>".format(name, test_he))
    else:
        userform = UserForm()
        return render(request, "calc.html", {"form": userform})
# Create your views here.

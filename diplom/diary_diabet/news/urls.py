from django.urls import path

from .views import *

urlpatterns = [
    path('',NewsStart.as_view(), name='index'),

]

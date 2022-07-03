from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Diary(models.Model):
    food_intake = models.ForeignKey('FIntake', on_delete=models.PROTECT, verbose_name='Прием пищи')
    glucoza = models.FloatField(max_length=255, verbose_name='Уровень глюкозы')
    he = models.FloatField(blank=True, verbose_name='Хлебные единицы')
    insulin = models.FloatField(verbose_name='Количество инсулина')
    food = models.TextField(blank=True, verbose_name="Употребляемая еда")
    date_food = models.DateField(verbose_name='Дата приема пищи')
    time_food = models.TimeField(verbose_name='Время приема пищи')
    datatime_inbase = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    dia_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    dok = models.CharField(max_length=255, blank=True, verbose_name='Доктор')

    def __str__(self):
        return str(self.datatime_inbase)

    def get_absolute_url(self):
        return reverse('show_record', kwargs={'id_user': self.id})

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = 'Записи'


class FIntake(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

from django.db import models
from django.urls import reverse


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Транслит заголовка')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    content = models.TextField(blank=True, verbose_name="Текст новости")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_published = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    author = models.CharField(max_length=150, default='Anonim', verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = 'Статьи'
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

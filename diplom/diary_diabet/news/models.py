from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_published = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=150, default='Anonim')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.name

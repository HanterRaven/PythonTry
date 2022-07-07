from django.db import models

# Create your models here.

class BaseFood(models.Model):
    c_name = models.CharField(max_length=255)
    c_he = models.CharField(max_length=255)
# Generated by Django 4.0.4 on 2022-07-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_pages', '0006_alter_diary_dia_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='dok',
            field=models.TextField(blank=True, verbose_name='Доктор'),
        ),
    ]

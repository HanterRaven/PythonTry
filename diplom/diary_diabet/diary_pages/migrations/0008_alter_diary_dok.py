# Generated by Django 4.0.4 on 2022-07-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_pages', '0007_diary_dok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='dok',
            field=models.CharField(blank=True, max_length=255, verbose_name='Доктор'),
        ),
    ]

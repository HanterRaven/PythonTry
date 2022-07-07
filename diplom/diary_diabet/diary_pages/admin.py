from django.contrib import admin

from .models import *
from django import forms


# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('glucoza',)}
    list_display = ('id','dia_user','food_intake','glucoza','he','insulin','food','date_food','time_food')
    list_display_links = ('id', 'glucoza','dia_user')
    list_editable = ('food_intake',)
    list_filter = ('date_food','dia_user')


admin.site.register(Diary,DiaryAdmin)
admin.site.register(FIntake)

admin.site.site_header = "Админ-панель дневника"
admin.site.site_title = "Админ-панель дневника"
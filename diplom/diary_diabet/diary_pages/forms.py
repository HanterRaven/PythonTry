from django import forms
from django.contrib.auth.models import User
from .models import *


class AddDiaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['food_intake'].empty_label = 'Категория не выбрана '
        # self.fields['dia_user'].empty_label = self.User.username

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 250:
    #         raise ValidationError('Длинна превышает 250 символов')
    #     return title

    # def add_user_d(self):
    #     if self.fields['dia_user'] == '':
    #         self.fields['dia_user'] = User

    class Meta:
        model = Diary
        fields = ['food_intake', 'glucoza', 'he', 'insulin', 'food', 'date_food', 'time_food']
        widgets = {
            'glucoza': forms.TextInput(attrs={'class': 'form-input'}),
            'he': forms.TextInput(attrs={'class': 'form-input'}),
            'insulin': forms.TextInput(attrs={'class': 'form-input'}),
            'food': forms.Textarea(attrs={'cols': 75, 'row': 20, 'class': 'form-input'}),
            'date_food': forms.DateInput(attrs={'class': 'form-input','type':"date"}),
            'time_food': forms.TimeInput(attrs={'class': 'form-input','type':"time"}),

        }

class Calc(forms.Form):
    name = forms.CharField(label='ведите продукт',max_length=255)
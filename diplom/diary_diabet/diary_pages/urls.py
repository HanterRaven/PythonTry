from django.urls import path

from .views import *

urlpatterns = [
    path('diary_page/', DiaryPage.as_view(), name='diary_page'),
    path('add_diary_page/', AddDiaryPage.as_view(), name='add_diary_page'),
    path('show_record/<int:id_user>/', ShowRecord.as_view(), name='show_record'),
    path('record_edit/<int:id_user>', RecordEdit.as_view(), name='record_edit'),
]

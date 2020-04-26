from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_todo),
    path('insert/',views.insert_list, name='insert_list'),
    path('delete/<int:todo_id>/',views.delete_list,name='delete_list')
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo),
    path('insert_todo', views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo')
]
from django.contrib import admin
from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('', TodoListView, name='home'),
]

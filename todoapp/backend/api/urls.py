from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='list'),
    path('todoscreate/', views.TodoListCreate.as_view(), name='list'),
    ]
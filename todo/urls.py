from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name = 'todo_list'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('todo/delete/<int:id>/', views.delete_todo, name = 'delete_todo')
]

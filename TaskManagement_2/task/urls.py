from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('show/', views.show_tasks, name='show_tasks'),
    path('task/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]

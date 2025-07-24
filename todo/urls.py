from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.updateTask, name='update'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
    path('view/<int:pk>/', views.viewTask, name='view'),
    path('edit/<int:pk>/', views.editTask, name='edit'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('view/<int:pk>/', views.view_board, name='view'),
    path('modify/<int:pk>/', views.modify, name='modify'),
    path('delete/<int:pk>/', views.delete_board, name='delete'),
]
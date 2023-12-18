from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crud/', views.crudPage, name="crud"),
    path('create-crud/', views.createCrud, name="create-crud"),
    path('update-crud/<str:pk>/', views.updateCrud, name="update-crud"),
    path('delete-crud/<str:pk>/', views.deleteCrud, name="delete-crud"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Routes, name = "routes"),
    path('user-list/', views.UserList, name = "user-list"),
    path('user-detail/<str:pk>/', views.Userdetail, name = "user-detail"),
    path('user-create/', views.UserCreate, name = "user-create"),
    path('user-update/<str:pk>', views.UserUpdate, name = "user-update"),

    path('user-delete/<str:pk>', views.UserDelete, name = "user-delete"),
    
] 
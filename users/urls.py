from django.contrib import admin
from django.urls import path
from . import views

app_name ='users' # Namespacing
urlpatterns = [
    path('createuser/', views.register,name='register'),
]
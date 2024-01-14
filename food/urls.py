from django.contrib import admin
from django.urls import path
from . import views

app_name ='food' # Namespacing
urlpatterns = [
    path('', views.index,name='index'),
    # /food/1-- detail food view
    path('<int:item_id>/',views.detail,name='detail'),
    path('about/', views.about,name='about'),
    path('add/', views.create_item,name='create_item'),
    path('update/<int:id>', views.update_item,name='update_item'),
    path('delete/<int:id>', views.delete_item,name='delete_item'),
]


print("BLOG URLS LOADED")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_post),
    path('delete/<int:id>/', views.delete_post),
    path('edit/<int:id>/', views.edit_post),
    path('test/', views.home),
]
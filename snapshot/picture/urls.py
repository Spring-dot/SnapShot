from django.contrib import admin
from django.urls import path
from . import views

app_name = 'picture'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('picture/add/', views.PictureCreate.as_view(), name='collect-add'),
]
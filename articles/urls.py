from django.urls import path
from . import views

# articles/____
urlpatterns = [
    path('', views.articles),
    path('create/', views.create),
    path('new/', views.new), 
    path('index/', views.index),
    path('<int:article_pk>/', views.detail),
]

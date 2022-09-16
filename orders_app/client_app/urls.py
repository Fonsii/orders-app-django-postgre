from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainScreen.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('search/', views.Search.as_view(), name='search'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('product/list', views.ProductsListView.as_view(), name='productsList'),
    path('product/create/', views.ProductsCreateView.as_view(), name='productsCreate'),
]

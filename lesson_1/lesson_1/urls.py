from django.contrib import admin
from django.urls import path

from product.api import ProductsListAPI, ProductsRetriveAPI

urlpatterns = [
    path('products', ProductsListAPI.as_view()),
    path('products/<int:pk>', ProductsRetriveAPI.as_view()),
]

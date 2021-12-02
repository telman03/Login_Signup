# -*- coding: utf-8 -*-
from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate

urlpatterns = [
    path('new/', ProductCreate.as_view(), name='product_new'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product_detail.html'),
    path('', ProductList.as_view(), name='product_list'),
]
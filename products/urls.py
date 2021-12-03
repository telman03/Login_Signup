from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductDelete, ProductUpdate

urlpatterns = [
    path('product/new/', ProductCreate.as_view(), name='product_new'),
    path('product/detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    path('product/edit/<int:pk>/', ProductUpdate.as_view(), name='product_edit'),
    path('', ProductList.as_view(), name='home'),
]
from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('product/detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('', ProductList.as_view(), name='home'),
]
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Product
# from .forms import ProductForm

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreate(CreateView):
    model = Product
    template_name = 'product_new.html' 
    fields = ['name', 'description', 'price']



class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    fields = ['name', 'description', 'price']


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')



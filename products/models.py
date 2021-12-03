# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)


    def __str__(self):
        return self.name

    def get_absolute_url(self): # new
        return reverse('product_detail', args=[str(self.id)])

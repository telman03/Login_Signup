# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    # created = models.DateTimeField('Created', auto_now_add=True)
    # changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', args=[str(self.id)])

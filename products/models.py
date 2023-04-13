from django.db import models
from vendor.models import Vendor


class Style(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 

class Category(models.Model):
  
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=10)
    friendly_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name   


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    style = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    sku = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

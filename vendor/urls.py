from django.urls import path
from . import views

urlpatterns = [
    path('vendor', views.vendor, name='vendor'),
    path('vendor_product_list', views.vendor_product_list, name='vendor_product_list'),
]
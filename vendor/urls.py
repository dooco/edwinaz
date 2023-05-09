from django.urls import path
from . import views

urlpatterns = [
    path('vendor', views.vendor, name='vendor'),
    path('become_vendor', views.become_vendor, name='become_vendor'),
    path('<int:product_id>/', views.vendor_product_detail, name='vendor_product_detail'),
    path('vendor_add_product/', views.vendor_add_product, name='vendor_add_product'),
    path('vendor_edit_product/<int:product_id>/', views.vendor_edit_product, name='vendor_edit_product'),
    path('vendor_delete_product/<int:product_id>/', views.vendor_delete_product, name='vendor_delete_product'),
]
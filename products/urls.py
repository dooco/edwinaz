""" Products URL """
from django.urls import path
from . import views
from .views import PostDetailView

""" Product URL """

urlpatterns = [
    path(
        '',
        views.all_products,
        name='products'),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'),
    path(
        'add/',
        views.add_product,
        name='add_product'),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path(
        'post/<int:pk>/',
        PostDetailView.as_view(),
        name='post_detail'),
]

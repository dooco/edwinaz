from django.urls import path
from . import views

"""
URL checkout
"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
]

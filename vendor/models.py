from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    """ Vendor model for holding information on vendor """
    name = models.CharField(max_length=255)
    created_by = models.OneToOneField(
       User, related_name='vendor', on_delete=models.CASCADE)
       
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

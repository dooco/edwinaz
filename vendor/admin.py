from django.contrib import admin

from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    """ Admin vendor list """
    list_display = (
        'name',
    )

    ordering = ('name',)



from django.contrib import admin

from .models import Product, Style, Category


class ProductAdmin(admin.ModelAdmin):
    """ Admin Product fields """
    list_display = (
        'sku',
        'name',
        'style',
        'price',
        'image',
    )

    ordering = ('sku',)


class StyleAdmin(admin.ModelAdmin):
    """ Admin Style Fields """
    list_display = (
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ Admin Category fields """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Category, CategoryAdmin)

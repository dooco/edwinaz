from django.contrib import admin

from .models import Product, Style, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'style',
        'price',
        'image',
    )

    ordering = ('sku',)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Category, CategoryAdmin)
